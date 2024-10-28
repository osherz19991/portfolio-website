from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = b'\xea%y\xf6\xfbG\x14ei\xc7\x887\x8c\x8e_\x15g\xa7\xa8\x16\xcf`\x8fw'  # Replace with the generated key

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'zafar.osher@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'wfwj kaoa yfoh ejyb'         # Replace with your email password

mail = Mail(app)

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route for the about page
@app.route("/about")
def about():
    return render_template("about.html")

# Route for the projects page
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Route for the contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Route to handle form submission
@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message_content = request.form.get("message")

    try:
        # Create and send the email
        msg = Message(
            subject=f"New message from {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=["zafar.osher@gmail.com"],
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}"
        )
        mail.send(msg)

        # Show a success message on the contact page
        flash("Your message has been sent successfully!", "success")

    except Exception as e:
        # Show an error message if something goes wrong
        flash(f"An error occurred while sending your message: {str(e)}", "error")

    # Render the contact page again with the message
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True)