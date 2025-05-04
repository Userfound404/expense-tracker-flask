import json
from app import create_app, db
from app.models import User, Category, Expense

app = create_app()
with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Load users
    users = json.load(open('sample_data/users.json'))
    for u in users:
        user = User(username=u['userid'])
        user.set_password(u['password'])
        db.session.add(user)
    db.session.commit()

    # Load categories
    categories = json.load(open('sample_data/categories.json'))
    for c in categories:
        # assuming each c has fields: userid, name
        user = User.query.filter_by(username=c['userid']).first()
        if user:
            cat = Category(name=c['name'], user_id=user.id)
            db.session.add(cat)
    db.session.commit()

    # Load expenses
    expenses = json.load(open('sample_data/expenses.json'))
    for e in expenses:
        # assuming each e has: userid, date, description, amount, category_name
        user = User.query.filter_by(username=e['userid']).first()
        cat = Category.query.filter_by(user_id=user.id, name=e['category_name']).first()
        if user and cat:
            exp = Expense(
                user_id=user.id,
                category_id=cat.id,
                date=e['date'],              # e.g. "2025-03-15"
                description=e['description'],
                amount=float(e['amount'])
            )
            db.session.add(exp)
    db.session.commit()

    print("Sample data loaded!")
