from flask import render_template, url_for, jsonify, flash, redirect, request
from sojiweb import app, db, mail, dev
from sojiweb.models import RealMessage, EmailList
from sojiweb.forms import ContactForm, NewsletterForm
from flask_mail import Message
import stripe
import os

if dev:
    from sojiweb.local_config import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY
else:
    from sojiweb.config import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY

# pylint: skip-file

stripe_keys = {
    "secret_key": STRIPE_SECRET_KEY,
    "publishable_key": STRIPE_PUBLISHABLE_KEY
}

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = NewsletterForm()
    if request.method == 'POST':
        if form.validate():
            email_data = EmailList(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
            db.session.add(email_data)
            db.session.commit()
            flash('Thank you for the message! We will return to you as shortly as possible.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Submission unsuccessful. Please retry.', 'danger')
            return redirect(url_for('home'))
    return render_template('index.html', title='Home', form=form)

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='About')

@app.route("/products", methods=['GET', 'POST'])
def products():
    return render_template('products.html', title='Products')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate():
            ### Message to us
            msg_to_us = Message("Automatic Message - %s %s says %s" % (form.first_name.data, form.last_name.data, form.subject.data),
                sender='sojiremora@gmail.com', recipients=['sojiremora@gmail.com'])
            msg_to_us.body = form.message.data
            mail.send(msg_to_us)

            ### Message to them
            msg_to_them = Message('Thank you for being interested in Soji', sender='sojiremora@gmail.com', 
                recipients=[form.email.data])
            msg_to_them.body = "Thank you for being interested in Soji. We will contact you shortly."
            mail.send(msg_to_them)
            
            if form.newsletter.data:
                email_data = EmailList(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
                db.session.add(email_data)
                db.session.commit()

            flash('Thank you for the message! We will return to you as shortly as possible.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Submission unsuccessful. Please retry.', 'danger')
    return render_template('contact.html', title='Contact', form=form)

# Flask + Stripe
@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "https://soji-website.herokuapp.com/"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "name": "Remora Shower Caddy",
                    "quantity": 1,
                    "currency": "usd",
                    "amount": "1100",
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route("/success")
def success():
    flash('Thank you for purchasing our product! Your product will arrive shortly. If you have any questions, feel free to Contact Us!', 'success')
    return render_template('products.html', title='Products')


@app.route("/cancelled")
def cancelled():
    flash('Payment Cancelled. Please try again.', 'danger')
    return render_template('products.html', title='Products')