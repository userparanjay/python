from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from jinja2 import Environment, FileSystemLoader
import os
from dotenv import load_dotenv

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)

env = Environment(loader=FileSystemLoader("templates"))

async def send_welcome_email(email: str, username: str):

    template = env.get_template("welcome_email.html")
    app_url = os.getenv("APP_URL", "http://localhost:3000")

    html_content = template.render(
        username=username,
        email=email,
        app_url=app_url
    )

    message = MessageSchema(
        subject="Welcome!",
        recipients=[email],
        body=html_content,
        subtype="html"
    )

    fm = FastMail(conf)

    await fm.send_message(message)


async def send_reset_password_email(email: str, reset_link: str):
    template = env.get_template("reset_password_email.html")

    html_content = template.render(
        reset_link=reset_link
    )

    message = MessageSchema(
        subject="Reset Password",
        recipients=[email],
        body=html_content,
        subtype="html"
    )

    fm = FastMail(conf)

    await fm.send_message(message)