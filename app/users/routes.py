from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
import app
from app.extensions import db, bcrypt
from app.users.models import User
from app.users.forms import SignUpForm, SignInForm
from werkzeug.utils import secure_filename
import uuid as uuid
import os



bp_users = Blueprint(
    name='users',
    import_name=__name__
)


@bp_users.route("/sign-up", methods=["GET", "POST"])
def sign_up():    
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(password=form.password.data).decode("utf-8")
        avatar_filename = secure_filename(filename=form.avatar.data.filename)
        avatar_filename_uuid = str(uuid.uuid4()) + avatar_filename
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            avatar=avatar_filename_uuid
        )
        db.session.add(user)
        db.session.commit()
        flash(message=f"Account '{form.username.data}' Created Successfully!", category="success")
        form.avatar.data.save(os.path.join(app.UPLOAD_FOLDER, avatar_filename_uuid))
        return redirect(location=url_for(endpoint="users.sign_in"))
    return render_template("users/sign-up.html", form=form)


@bp_users.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if current_user.is_authenticated:
        return redirect(location=url_for(endpoint="dashboard.dashboard"))
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(pw_hash=user.password, password=form.password.data):
            login_user(user=user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page if next_page else url_for(endpoint="dashboard.dashboard"))
        else:
            flash(message="Email or Password is Incorrect!", category="danger")
    return render_template("users/sign-in.html", form=form)


@bp_users.route("/sign-out")
@login_required
def sign_out():
    logout_user()
    return redirect(location=url_for(endpoint="users.sign_in"))