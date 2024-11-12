# Dealing with Static Files in Django
Static files such as CSS, JS, and Images are crucial for formatting and organizing web pages and should be considered in every application. In Django, managing static files served to a web page during development and production is easy. Django provides a tool called `django.contrib.staticfiles` to help with this; it should be included in `INSTALLED_APPS` in `settings` module of any project.

## Organization
In any APP, define a directory/folder named `static` and then include another folder inside it that matches the name of your APP.
