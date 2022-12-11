from flask import Blueprint, flash, redirect, render_template, url_for, request
from register import RegistrationForm
from user import User
from app import db


# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    # static_folder='static'
)


@auth_bp.route("/signup", methods=["GET", "POST"])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                username=form.username.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            # login_user(user)  # Log in as newly created user
            return redirect(url_for('books'))
        flash('That user already exists')
    return render_template(
        'signup',
        title='Create an Account.',
        form=form,
        template='signup',
        body="Sign up for a user account."
    )