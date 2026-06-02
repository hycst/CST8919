import os
from urllib.parse import urlencode

from dotenv import load_dotenv
from flask import Flask, redirect, session, url_for, render_template_string
from authlib.integrations.flask_client import OAuth

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("AUTH0_SECRET")

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=os.getenv("AUTH0_CLIENT_ID"),
    client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{os.getenv('AUTH0_DOMAIN')}/.well-known/openid-configuration",
)


@app.route("/")
def home():
    user = session.get("user")

    return render_template_string("""
    <h1>CST8919 Lab 1 - Flask Auth0 Login</h1>

    {% if user %}
        <p>Welcome, {{ user.name }}!</p>
        <a href="/protected">Protected Page</a><br>
        <a href="/logout">Logout</a>
    {% else %}
        <a href="/login">Login with Auth0</a>
    {% endif %}
    """, user=user)


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/callback")
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token.get("userinfo")
    return redirect("/")


@app.route("/protected")
def protected():
    if "user" not in session:
        return redirect(url_for("login"))

    user = session["user"]

    return render_template_string("""
    <h1>Protected Page</h1>
    <p>You are logged in.</p>
    <p>Name: {{ user.name }}</p>
    <p>Email: {{ user.email }}</p>
    <a href="/">Home</a><br>
    <a href="/logout">Logout</a>
    """, user=user)


@app.route("/logout")
def logout():
    session.clear()

    params = {
        "returnTo": url_for("home", _external=True),
        "client_id": os.getenv("AUTH0_CLIENT_ID"),
    }

    return redirect(
        f"https://{os.getenv('AUTH0_DOMAIN')}/v2/logout?"
        + urlencode(params)
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)