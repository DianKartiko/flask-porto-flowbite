from flask import Blueprint, render_template

# --- Blueprint Initiation ---
bp = Blueprint("route", __name__)

# --- Blurprint Route ---
@bp.route("/")
def index():
    return render_template("index.html")
