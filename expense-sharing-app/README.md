# Expense Sharing Application

## Overview
The Expense Sharing Application allows users to manage their daily expenses and share costs with friends or family. It supports various splitting methods (equal, exact, percentage) and provides functionalities to track individual and overall expenses.

## Features
- User management (Each user should have an email, name, and mobile number)
- Expense management (users can add expenses)
- Split expenses using different methods:
  - Equal
  - Exact
  - Percentage
- Generate and download balance sheets
- Retrieve individual user expenses
- Retrieve overall expenses

## Prerequisites
- Python 3.6 or higher
- Flask
- Flask-SQLAlchemy (for database management)
- A virtual environment (optional but recommended)

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Kartik-Jagdale/expense-sharing-app.git
   cd expense-sharing-app

## Create a Virtual Environment (optional)
source venv/bin/activate

## Run application
python3 app.py

## ---------------------API Endpoints-----------------------------
## -------------for create user ----------------------------------
 curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{"name": "kartik", "email": "kartik@2022.com"}'

## ----------------For create expences ---------------------------
curl -X POST http://127.0.0.1:5000/expenses \
-H "Content-Type: application/json" \
-d '{
  "description": "Dinner with friends",
  "amount": 2000,
  "split_type": "equal",
  "participants": [
    {"user_id": 1, "name": "kartik"},
    {"user_id": 2, "name": "xyz"}
  ],
  "user_id": 1
}'



## ----------------------- For Getting details of users -----------------

curl -X GET http://127.0.0.1:5000/users 


## ----------------------- For Getting details of individual user expenses -------------

curl -X GET http://127.0.0.1:5000/users/1/expenses


## ----------------------- For Getting details of all user expenses -------------

curl -X GET http://127.0.0.1:5000/expenses

## ----------------------- For  Download Balance Sheet-------------

curl -X GET http://127.0.0.1:5000/balance_sheet


