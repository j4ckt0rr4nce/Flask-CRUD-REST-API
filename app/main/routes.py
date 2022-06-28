from . import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from .forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from .model.user import User


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='Home')


@app.route('/service', methods=['GET', 'POST'])
@login_required
def service():
    return render_template('service.html', title='Service')


@app.route('/customers_service', methods=['GET', 'POST'])
@login_required
def customer():
    return render_template('customer.html', title='Customer')


@app.route('/addresses_service', methods=['GET', 'POST'])
@login_required
def address():
    return render_template('address.html', title='Address')


@app.route('/orders_service', methods=['GET', 'POST'])
@login_required
def order():
    return render_template('order.html', title='Order')


@app.route('/items_service', methods=['GET', 'POST'])
@login_required
def item():
    return render_template('item.html', title='Item')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('service'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('service'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', category='danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('service')
        flash(f'Success! You are logged in as: {user.username}', category='success')   
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('service'))


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('service'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('service'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('service'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)
