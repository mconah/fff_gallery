from flask import Flask, render_template, redirect, request, url_for, send_file, send_from_directory, flash
from flask import g
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pathlib import Path
import os
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/social-channel")
def social():
    return render_template("social.html")

@app.route("/gallery")
@app.route("/")
def gallery():
    return render_template("gallery.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("notfound.html"), 404

@app.errorhandler(500)
def internal_server(error):
    return render_template("servererror.html"), 500

if __name__ == "__main__":
    app.run(debug=True)