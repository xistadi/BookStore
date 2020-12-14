# BookStore
[![made-with-django](https://img.shields.io/badge/Made%20with-Django-2cc737.svg)](https://www.djangoproject.com) [![website](https://img.shields.io/badge/Web%20Site-PythonAnywhere-blue.svg)](http://xistadi.pythonanywhere.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/ab24db?icon=github)](https://github.com/xistadi/BookStore) [![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://www.donationalerts.com/c/xistadi)

**«BookStore»** - is an electronic store, intended for selling paper books on-line via the Internet.
The development process included writing a backend web application using the Django framework (with additional libraries), a frontend using HTML/CSS/Bootstrap/Javascript.

![gif](https://github.com/xistadi/BookStore/blob/master/images/start.gif)
---

## Features

- Groups of users with permissions(Admin, Managers, Customers)
- Administrative portal
- Built-in administrative portal
- Shopping cart
- Order
- Promotions
- Product rating
- Reviews
- User profiles
- CRUD(l) for each of the listed
- The application is covered by Unit tests

## How to start

1. Clone project from github
    ```
    git clone https://github.com/xistadi/BookStore
    ```
2. Create `venv`
    ```zsh
    #Linux/Mac
    python3 -m venv env
    ```
    ```bash
    #Win cmd
    python -m venv env
    ```
3. Activate `venv`
4. Install requirements
    ```
    pip install -r requirements.txt
    ```
5. Create folder `media` and `static_dev`
6. Go to src/proj/
    - Create my_local_settings.py
        ```
        STATIC_ROOT = '*Here is your direction to project* \\static'
        MEDIA_ROOT = '*Here is your direction to project* \\media'
        STATICFILES_DIRS = (
        	'*Here is your direction to project* \\static_dev',
        )
        EMAIL_HOST_USER = 'Your email'
        EMAIL_HOST_PASSWORD = 'Your email password'
        ```
    - Create secrets.py
        ```
        SECRET_KEY = 'wa5dgjxynoz1iygl99-q@gl#-*%@hc%k4d7e#xqukg=5ql)q'
        ```
7. Go to src/
    - Make migrations
        ```
        python manage.py migrate
        ```
    - Run server
        ```
        python manage.py runserver
        ```
8. Open your web browser http://127.0.0.1:8000

## How to start unit test

1. Go to src/
    ```
    python manage.py test .
    ```
2. **You'r great**

## Useful links

- [Django Documentation](https://docs.djangoproject.com/en/3.1/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/4.5/)
- [Unit test](https://docs.python.org/3/library/unittest.html)
- [NProgress](https://github.com/rstacruz/nprogress)
