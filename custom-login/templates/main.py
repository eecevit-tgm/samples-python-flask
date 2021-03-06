import json
import time

from flask import Flask, render_template, url_for, redirect
from flask_oidc import OpenIDConnect

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'OIDC_CLIENT_SECRETS': '../client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_SCOPES': ["openid", "profile", "email"],
    'OIDC_CALLBACK_ROUTE': '/authorization-code/callback'
})

oidc = OpenIDConnect(app)


@app.route("/")
def home():
    return 'HALLO'


@app.route("/api/messages")
@oidc.accept_token(True)
def messages():
    response = {
        'messages': [
            {
                'date': time.time(),
                'text': 'I am a robot.'
            },
            {
                'date': time.time()-3600,
                'text': 'Hello, World!'
            }
        ]
    }

    return json.dumps(response)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
