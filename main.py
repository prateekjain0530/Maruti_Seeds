from flask import Flask,render_template,request,make_response,session
from flask import redirect,url_for
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/services/")
def services():
    return render_template("services.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/mail/",methods=["POST","GET"])
def mail():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        messages = request.form.get("message")
        try:
            if request.method == "POST":
                from_email = "perfectwellness7181@gmail.com"
                to_email = "perfectwellness7181@gmail.com"
                p = "perfectwellness@123"
                message = MIMEMultipart("alternative")
                message["Subject"] = "Mail from"
                message["To"] = to_email
                message["From"] = from_email
                html = f"""
                <h3><strong> Name </strong> = {name}<br></h3>
                <h3><strong> Email </strong> = {email}<br></h3>
                <h3><strong> Phone </strong> = {phone}<br></h3>
                <h3><strong> Message </strong> = {messages}<br></h3>
                """
                msg = MIMEText(html,"html")
                message.attach(msg)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
                    server.login(from_email,p)
                    server.sendmail(from_email,to_email,message.as_string())
            else:
                return ("mail not sent")
        except Exception as e:
            return f"{e}"
        else:
            return render_template("index.html")

app.run()



