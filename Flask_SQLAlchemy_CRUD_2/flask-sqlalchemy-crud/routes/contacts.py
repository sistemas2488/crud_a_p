from flask import Blueprint, render_template, request, redirect, url_for, flash,jsonify
from models.contact import Contact
from utils.db import db
from flask_cors import CORS, cross_origin


contacts = Blueprint("contacts", __name__)

@cross_origin
@contacts.route("/")
def iprincipal():
     return jsonify({"informacion":"Principal"})

@cross_origin
@contacts.route('/getAll')
def index():
    contacts = Contact.query.all()
    print(len(contacts))
    payload = [] 
    content = {}
    for i in range(len(contacts)):
        content = {'id': contacts[i].id, 'fullname': contacts[i].fullname, 'email': contacts[i].email, 'phone': contacts[i].phone}
        payload.append(content)
        content = {}
    return jsonify(payload)

@cross_origin
@contacts.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        # receive data from the form
        fullname = request.json['fullname']
        email = request.json['email']
        phone = request.json['phone']
        # create a new Contact object
        new_contact = Contact(fullname, email, phone)
        # save the object into the database
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"informacion":"Contact added successfully!"})

@cross_origin
@contacts.route("/update/<string:id>", methods=["PUT"])
def update(id):
    # get contact by Id
    print(id)
    contact = Contact.query.get(id)
    contact.fullname = request.json['fullname']
    contact.email = request.json['email']
    contact.phone = request.json['phone']
    db.session.commit()
    return jsonify({"informacion":"Contact updated successfully!"})

        

@cross_origin
@contacts.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"informacion":"Contact delete successfully!"})




