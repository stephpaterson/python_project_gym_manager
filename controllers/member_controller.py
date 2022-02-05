from flask import Flask, render_template, request, redirect, Blueprint

import repositories.member_repository as member_repo
from models.member import Member

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route('/members', methods=['GET'])
def show():
    members = member_repo.select_all()
    return render_template('/member/index.html', members=members)

@members_blueprint.route('/members/new', methods=['GET'])
def new_member():
    return render_template('/member/new.html')

@members_blueprint.route('/members', methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    member = Member(first_name, last_name, phone_number, email)
    member_repo.save(member)
    return redirect('/members')
