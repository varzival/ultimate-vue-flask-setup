from flask import Blueprint, request, session

api_bp = Blueprint("api", __name__,
            static_folder = "../dist/static",
            template_folder = "../dist")

@api_bp.route("/greetings")
def greetings():
    return { "text": "Hello from Flask!" }

@api_bp.route("/login")
def login():
    name = request.args.get("username", None)
    if not name:
        return "no username given", 400
    session["username"] = name
    return "success"

@api_bp.route("/logout")
def logout():
    if "username" in session:
        del session["username"]
    return "success"

@api_bp.route("/myname")
def myname():
    if "username" in session:
        return { "username": session["username"] }
    return { "text": "Please login first." }