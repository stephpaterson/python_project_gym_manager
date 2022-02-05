from flask import Flask, render_template, request, redirect, Blueprint

import repositories.member_repository as member_repo
from models.member import Member

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route('/members')
def show():
    members = member_repo.select_all()
    return render_template('/member/index.html', members=members)