from flask import Blueprint, render_template

module = Blueprint('appname', __name__, template_folder="templates")


@module.route('/')
def index():
    return render_template("appname/index.html")


@module.route('/create')
def create():
    return render_template("appname/create.html")


@module.route('/list')
def list():
    return render_template("appname/list.html")


@module.route('/update')
def update():
    return render_template("appname/update.html")


@module.route('/delete')
def delete():
    return render_template("appname/delete.html")
