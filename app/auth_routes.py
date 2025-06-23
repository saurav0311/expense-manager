from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import db, User
from .import bcrypt
from flask_login import login_user
from flask_login import logout_user
auth=Blueprint("auth",__name__)

@auth.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username= request.form.get("username")
        email= request.form.get("email")
        password= request.form.get("password")
        existing_user= User.query.filter((User.username == username) | (User.email==email)).first()# | -> OR Operator
        if existing_user:
            flash("User already exists!!", category="danger")
            return redirect(url_for("auth.register"))
        hashed_password= bcrypt.generate_password_hash(password).decode("utf-8")
        new_user= User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("User registered successfully!!!", category="success")
        return redirect(url_for("main.dashboard"))
    return render_template("register.html")

from flask import session
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password= request.form.get("password")
        user= User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user) # session["user_id"]=user.id
            # session["username"]=user.username
            flash("Login Successful!!!", category="success")
            return redirect(url_for("main.home"))
        else:
            flash("Invalid. Try again!!", category="danger")
            return redirect(url_for("auth.login"))
    return render_template("login.html")
@auth.route("/logout")
def logout():
    logout_user()
    flash("Logged out successfully.", category="danger")
    return redirect(url_for('auth.login'))