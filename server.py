from flask import Flask, flash, session, request, redirect, render_template
from db.data_layer import get_all_bills, get_bill, create_bill, delete_bill, update_bill

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
