### CST8919 Lab 1 - Flask Auth0 Login

#### Features

- Auth0 Login
- Auth0 Logout
- Protected Route
- Session Management

#### Setup

1. Clone repository

2. Create virtual environment

```bash
python -m venv venv
```

#### Activate environment
venv\Scripts\activate

#### Install dependencies
```bash
pip install flask authlib python-dotenv requests
```

#### Configure .env
AUTH0_DOMAIN=hycst.ca.auth0.com

AUTH0_CLIENT_ID=bDjHxws4eZfabTDaYZlqQadY4knIHlUz

AUTH0_CLIENT_SECRET=6e4vQNd5Jq2pXef2Q2ucKDzfG_580_F4iV04z3b0Ne4XtCIt5np94NlT4-IjCyBg

AUTH0_SECRET=mysecretkey

AUTH0_REDIRECT_URI=http://localhost:5000/callback


#### Run application
```bash
python app.py
```
