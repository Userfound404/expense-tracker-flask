from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, current_app
from flask_login import login_required, current_user
from app.forms import ExpenseForm, CategoryForm, DeleteForm
from app.models import Expense, Category
from app import db
from sqlalchemy import func

exp_bp = Blueprint('exp', __name__)

@exp_bp.route('/')
@login_required
def dashboard():
    # Forms
    exp_form = ExpenseForm()
    exp_form.category.choices = [(c.id, c.name) for c in current_user.categories]
    cat_form = CategoryForm()
    delete_form = DeleteForm()

    # Raw data
    expenses   = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).all()
    categories = current_user.categories

    # Summary metrics
    total_spent = db.session.query(func.coalesce(func.sum(Expense.amount), 0))\
                    .filter(Expense.user_id==current_user.id).scalar()
    budget     = current_app.config['DEFAULT_BUDGET']
    money_left = budget - total_spent

    return render_template(
        'expenses/dashboard.html',
        exp_form=exp_form,
        cat_form=cat_form,
        delete_form=delete_form,
        expenses=expenses,
        categories=categories,
        total_spent=total_spent,
        money_left=money_left
    )

@exp_bp.route('/expense/create', methods=['POST'])
@login_required
def create_expense():
    form = ExpenseForm()
    form.category.choices = [(c.id, c.name) for c in current_user.categories]
    if form.validate_on_submit():
        e = Expense(
            date=form.date.data,
            description=form.description.data,
            amount=float(form.amount.data),
            category_id=form.category.data,
            user_id=current_user.id
        )
        db.session.add(e)
        db.session.commit()
        flash('Expense added', 'success')
    else:
        flash('Error: please check your input', 'danger')
    return redirect(url_for('exp.dashboard'))

@exp_bp.route('/category/create', methods=['POST'])
@login_required
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        c = Category(name=form.name.data, user_id=current_user.id)
        db.session.add(c)
        db.session.commit()
        flash('Category created', 'success')
    else:
        flash('Error: please check category name', 'danger')
    return redirect(url_for('exp.dashboard'))

# Optional: JSON summary endpoint for Chart.js
@exp_bp.route('/api/summary')
@login_required
def summary():
    # Sum of expenses by category for the current year
    year = func.extract('year', func.current_date())
    results = (db.session.query(Category.name, func.sum(Expense.amount))
               .join(Expense)
               .filter(Expense.user_id==current_user.id,
                       func.extract('year', Expense.date)==year)
               .group_by(Category.name).all())
    return jsonify({
        'labels': [r[0] for r in results],
        'values': [float(r[1]) for r in results]
    })

@exp_bp.route('/expense/delete/<int:expense_id>', methods=['POST'])
@login_required
def delete_expense(expense_id):
    exp = Expense.query.filter_by(id=expense_id, user_id=current_user.id).first_or_404()
    db.session.delete(exp)
    db.session.commit()
    flash('Expense deleted', 'success')
    return redirect(url_for('exp.dashboard'))

@exp_bp.route('/expense/edit/<int:expense_id>', methods=['GET', 'POST'])
@login_required
def edit_expense(expense_id):
    exp = Expense.query.filter_by(id=expense_id, user_id=current_user.id).first_or_404()
    form = ExpenseForm(obj=exp)
    form.category.choices = [(c.id, c.name) for c in current_user.categories]

    if form.validate_on_submit():
        exp.date         = form.date.data
        exp.description  = form.description.data
        exp.amount       = float(form.amount.data)
        exp.category_id  = form.category.data
        db.session.commit()
        flash('Expense updated', 'success')
        return redirect(url_for('exp.dashboard'))

    return render_template('expenses/edit_expense.html', form=form, expense=exp)

import csv
from io import StringIO
from flask import Response

@exp_bp.route('/export')
@login_required
def export_expenses():
    # Prepare in-memory CSV
    buffer = StringIO()
    writer = csv.writer(buffer)
    writer.writerow(['Date','Category','Description','Amount'])

    rows = Expense.query.filter_by(user_id=current_user.id)\
                        .order_by(Expense.date).all()
    for e in rows:
        writer.writerow([
            e.date.isoformat(),
            e.category.name,
            e.description,
            f"{e.amount:.2f}"
        ])

    # Build response
    output = buffer.getvalue()
    buffer.close()
    return Response(
        output,
        mimetype='text/csv',
        headers={
          'Content-Disposition': 'attachment; filename=expenses.csv'
        }
    )
