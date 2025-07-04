from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from forms import BookingForm, LoginForm
from models import db, Booking, User
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

load_dotenv()  # <- this loads the .env file
def seed_admin():
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', password=generate_password_hash('beauty123'))
            db.session.add(admin)
            db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/book', methods=["GET", "POST"])
def book():
    form = BookingForm()
    if form.validate_on_submit():
        try:
            dt = datetime.strptime(form.datetime.data, "%Y-%m-%d %H:%M")
            new_booking = Booking(
                name=form.name.data,
                service=form.service.data,
                datetime=dt
            )
            db.session.add(new_booking)
            db.session.commit()
            flash("Booking confirmed!", "success")
            return redirect("/")
        except Exception as e:
            db.session.rollback()
            flash("Error saving booking. Try again.", "danger")
    return render_template("book.html", form=form)

@app.route("/admin")
@login_required
def admin():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    bookings = Booking.query.order_by(Booking.datetime).paginate(page=page, per_page=per_page)

    return render_template("admin.html", bookings=bookings)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect("/admin")
        flash("Invalid username or password", "danger")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect("/")

@app.route("/admin/edit/<int:booking_id>", methods=["GET", "POST"])
@login_required
def edit_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    form = BookingForm(obj=booking)

    if form.validate_on_submit():
        try:
            booking.name = form.name.data
            booking.service = form.service.data
            booking.datetime = datetime.strptime(form.datetime.data, "%Y-%m-%d %H:%M")
            db.session.commit()
            flash("Booking updated successfully.", "success")
            return redirect("/admin")
        except Exception:
            db.session.rollback()
            flash("Update failed. Try again.", "danger")

    form.datetime.data = booking.datetime.strftime("%Y-%m-%d %H:%M")
    return render_template("book.html", form=form)

@app.route("/admin/delete/<int:booking_id>", methods=["GET"])
@login_required
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    try:
        db.session.delete(booking)
        db.session.commit()
        flash("Booking deleted.", "info")
    except Exception:
        db.session.rollback()
        flash("Failed to delete booking.", "danger")
    return redirect("/admin")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_admin()
    app.run(debug=True)

