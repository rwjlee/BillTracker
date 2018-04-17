from flask import Flask, flash, session, request, redirect, render_template, url_for
from db.data_layer import get_all_bills, get_bill, create_bill, delete_bill, update_bill

app = Flask(__name__)

@app.route('/')
def index():
    db_bills = get_all_bills()
    return render_template('index.html', bills = db_bills)

@app.route('/add_bill', methods=['POST'])
def add_bill():
    server_description = request.form['html_description']
    server_amount = request.form['html_amount']
    create_bill(server_amount, server_description)
    return redirect(url_for('index'))

@app.route('/edit_bill/<bill_id>')
def edit_bill(bill_id):
    db_bill = get_bill(bill_id)
    return render_template('edit.html', bill=db_bill)

@app.route('/update_bill', methods=['POST'])
def update_bill_request():
    update_bill(request.form['html_id'], request.form['html_amount'], request.form['html_description'])
    return redirect(url_for('index'))

@app.route('/delete_bill/<bill_id>')
def delete_bill_request(bill_id):
    delete_bill(bill_id)
    return redirect(url_for('index'))

app.run(debug = True)