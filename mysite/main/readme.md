# main

`main` is our app being developed within the project. The app lets users make to do lists and items on the to do lists.

this directory includes all the python files that define this app: 

- `admin.py` is stuff that displays on the admin dashboard
- `apps.py` was automatically created when creating the app
- `forms.py` defines the forms and the fields within
- `models.py` defines the data model of items in `forms.py`
- `tests.py` was automatically created when creating the app
- `urls.py` tells the broser what to do when the user goes to certain paths at the url. It relates to `views.py`
- `views.py` has functions that define all the actions performed when users go to urls and do stuff on the site like fill out the forms
- `templates/` has all of the html pages of the site. In them you will see brackets with parentheses `{% ... %}`. This is how django dynamically displays content on the web pages.