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

#### Configure .env  (the values have been removed)
AUTH0_DOMAIN=************

AUTH0_CLIENT_ID=************

AUTH0_CLIENT_SECRET=************

AUTH0_SECRET=************

AUTH0_REDIRECT_URI=http://localhost:5000/callback


#### Run application
```bash
python app.py
```
