from flask import Flask, request, jsonify
from models import db, User, Expense
from flask_migrate import Migrate

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Daily Expenses Sharing Application!'})

# Create User Endpoint
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'error': 'User with this email already exists'}), 400  

    if not data.get('name') or not data.get('email') or not data.get('mobile'):
        return jsonify({'error': 'Missing required fields'}), 400

    new_user = User(name=data['name'], email=data['email'], mobile=data['mobile'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201

# Retrieve User Details
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'mobile': user.mobile
    } for user in users]), 200

# Add Expense
@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    participants = data.get('participants', [])
    
    if len(participants) == 0:
        return jsonify({'error': 'No participants provided'}), 400

    # Calculate how to split the expense
    if data['split_type'] == 'equal':
        split_amount = data['amount'] / len(participants)
        for participant in participants:
            participant['amount'] = split_amount
    elif data['split_type'] == 'percentage':
        total_percentage = sum([p['percentage'] for p in participants])
        if total_percentage != 100:
            return jsonify({'error': 'Percentages must add up to 100%'}), 400
        for participant in participants:
            participant['amount'] = data['amount'] * (participant['percentage'] / 100)
    elif data['split_type'] == 'exact':
        total_amount = sum([p['amount'] for p in participants])
        if total_amount != data['amount']:
            return jsonify({'error': 'Exact amounts do not sum to total amount'}), 400
    
    # Create the expense
    new_expense = Expense(
        description=data['description'], 
        amount=data['amount'],
        split_type=data['split_type'], 
        participants=participants,  # Assuming JSON column
        user_id=data['user_id']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully', 'expense_id': new_expense.id}), 201

# Retrieve User Expenses
@app.route('/users/<int:user_id>/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([{
        'id': expense.id,
        'description': expense.description,
        'amount': expense.amount,
        'split_type': expense.split_type,
        'participants': expense.participants,
        'user_id': expense.user_id
    } for expense in expenses]), 200


if __name__ == '__main__':
    app.run(debug=True)

