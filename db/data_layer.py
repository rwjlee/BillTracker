from db.base import DbManager
from db.entities import BillItem

db = DbManager()

def get_all_bills():
    return db.open().query(BillItem).all()

def get_bill(bill_id):
    return db.open().query(BillItem).filter(BillItem.id == bill_id).one()

def create_bill(amount, description):
    bill = BillItem()
    bill.amount = amount
    bill.description = description
    db.save(bill)

def delete_bill(bill_id):
    bill = db.open().query(BillItem).filter(BillItem.id == bill_id).one()
    db.delete(bill)

def update_bill(bill_id, amount, description):
    bill = db.open().query(BillItem).filter(BillItem.id == bill_id).one()
    bill.amount = amount
    bill.description = description
    db.save(bill)

