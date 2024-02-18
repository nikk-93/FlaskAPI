import os
from flask import Flask, redirect, render_template, request, session, flash, url_for
from login import SignUpForm, SignInForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/base/')
def base_template():
    return render_template(template_name_or_list='base.html')


@app.route('/sign_up/', methods=["GET", "POST"])
def sign_up():
    sign_up_form = SignUpForm()

    if sign_up_form.validate_on_submit():
        flash("SignUp was successful, please login")
        return redirect(url_for('sign_in'))

    return render_template(template_name_or_list='sign_up.html',
                           form=sign_up_form)


@app.route('/sign_in/', methods=["GET", "POST"])
def sign_in():
    sign_in_form = SignInForm()

    if sign_in_form.validate_on_submit():
        flash("SignIn was successful")
        session["email"] = request.form.get("email")
        return redirect(url_for('welcome'))

    return render_template(template_name_or_list='sign_in.html',
                           form=sign_in_form)


@app.route('/welcome/')
def welcome():
    return render_template('welcome.html', user=session["email"])


@app.route('/sign_out/', methods=["GET", "POST"])
def sign_out():
    session.pop("email", None)
    return redirect(url_for('index'))


if __name__ == '__main__':

    app.run(debug=True)
