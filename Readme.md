# Django tutorial
Following a youtube tutorial to configure a website app for users to make to do lists. Incolves configuring django itself, a database, and web pages with dynamic forms.


from: https://www.youtube.com/watch?v=Z4D3M-NSN58&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9&index=2

## to get started

1. clone repo, open a terminal window, navigate to this repo `../django_tutorial/mysite`
2. install django: `pip install django`
3. install pipenv: `pip install pipenv`
4. install crispy forms `pip install django-crispy-forms` and `pip install crispy-bootstrap5`
5. launch a virtual environment: `python -m pipenv shell` 
6. *optional* - open VScode of directory to see contents & what's going on. `code .`
7. now you can lrun a local server to view the web app with `python manage.py runserver`. Terminal should tell you where the server is running. Open an internet browser window and go to the listed address, probably http://127.0.0.1:8000/