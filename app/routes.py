from flask import Blueprint, render_template, request, redirect
from .models import db, Expense
from flask_login import current_user
from flask_login import login_required

main= Blueprint("main",__name__)
@main.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method=="POST":
        amount=request.form.get("amount")
        category=request.form.get("category")
        note=request.form.get("note")
        amount = float(amount) 

        new_expense=Expense(amount=amount,
                            category=category,
                            note=note,
                            user_id= current_user.id)
        db.session.add(new_expense)
        db.session.commit()
        return redirect("/dashboard")
    expenses=Expense.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", expenses=expenses)

@main.route("/")
def landing_page():
    return render_template("landing.html")
 
