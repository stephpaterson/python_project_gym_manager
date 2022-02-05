from re import M
from flask import Flask, render_template, request, redirect, Blueprint

import repositories.member_repository as member_repo
from models.member import Member

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route('/members')
def show_all():
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

@members_blueprint.route("/members/<id>", methods=['GET'])
def show_member(id):
    member = member_repo.select_by_id(id)
    return render_template('/member/show.html', member=member)

@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    member = member_repo.select_by_id(id)
    return render_template('/member/edit.html', member=member)

@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    member = Member(first_name, last_name, phone_number, email, id)
    member_repo.update(member)
    return redirect('/members')

@members_blueprint.route("/members/<id>/delete")
def delete_member(id):
    member_repo.delete(id)
    return redirect('/members')