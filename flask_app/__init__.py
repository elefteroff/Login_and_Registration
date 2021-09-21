from flask import Flask
app = Flask(__name__)
app.secret_key = "secretlogin"

DATABASE_SCHEMA = 'Login_Reg'