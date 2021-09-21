from flask_app import app, DATABASE_SCHEMA
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app)     

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        new_users_id = connectToMySQL(DATABASE_SCHEMA).query_db(query,data)
        return new_users_id

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if results:
            all_users = []
            for users in results:
                all_users.append(cls(users))
            return all_users

    @classmethod
    def get_one(cls, **data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query,data)
        if results:
            return cls(results[0])
        return results

    @classmethod
    def get_one_email(cls, **data):
        '''Takes in an email and returns a User object'''
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query,data)
        if results:
            return cls(results[0])
        return results

# ********************* VALIDATIONS *********************

    @staticmethod
    def validate_users(data):
        is_valid = True

        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters.", "error_first_name")
            is_valid = False

        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters.", "error_last_name")
            is_valid = False

        if len(data['email']) < 6:
            flash("Email must be 6 or greater.", "error_email")
            is_valid = False

        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(data['password']) < 3:
            flash("Password must be at least 8 characters.", "error_password")
            is_valid = False

        if len(data['confirm_password']) < 3:
            flash("Confirm Password.", "error_confirm_password")
            is_valid = False

        return is_valid



