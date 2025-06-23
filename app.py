from flask import Flask, render_template, request, redirect
app=Flask(__name__)
expenses=[]
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="POST":
        amount=request.form.get("amount")
        category=request.form.get("category")
        note=request.form.get("note")

        expense={
            "amount":amount,
            "category":category,
            "note":note,
        }
        expenses.append(expense)
        return redirect("/")
    return render_template("index.html", expenses=expenses)
if __name__=="__main__":
    app.run(debug=True)