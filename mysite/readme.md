# mysite

so `mysite` is the project. `main` is an app within the project.

They are related through `mysite/urls.py`, which points to `main/urls.py`, which points to all the view functions defines in `main/views.py`.

`main/views.py` is important because in django, a "view" is an action or a request handler. It's not viewing anything. Rather, a view is what gets returned to the user viewing the site, including dynamic stuff like what happens when a user submits a form. 


`manage.py` gets called a lot from the terminal to configure a virtual environment and then launch a virtual server to see what the website looks like as you're developing it. 

to run the server, in terminal navigate to this directory and:
```
python manage.py runserver
```
It will tell you the address to view the server in a browser window.