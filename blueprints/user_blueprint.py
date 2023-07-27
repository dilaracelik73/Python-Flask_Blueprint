from flask import Blueprint, render_template

#bu ve product_blueprint için blueprints adında dosya açılacak. App üzerinden bağlantı sağlanacak,import ile.
#blueprint ile yönlendirmeyi app.py dosyası üzerinden yapabiliriz.

user_bp = Blueprint("user_bp", __name__)
@user_bp.route("/")
def show_users():
    users = ["dilara", "elif", "huri", "nuri"]
    return render_template("users.html", users=users)

@user_bp.route("/<username>")
def show_user(username):
    return f"User Name : {username}"