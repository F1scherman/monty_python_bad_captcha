This is a Django app I made to compete in a widget contest
with the prompt "Bad CAPTCHAs", as well as to learn a bit
of Django along the way.

The captcha questions are based on the legendary part in The
Holy Grail where King Arthur and Co need to cross the bridge.

This isn't a true webapp, I'm just using the development server
to mimic one. To run it, use the command `python manage.py runserver`,
but you may need to install Django before that works. If you have
access to Pycharm, I believe it will handle everything for you and you
can just hit play. You can then access the captchas at `localhost:8000/captcha/`,
you can also access the admin panel to edit the database of questions at
`localhost:8000/admin/` with username `admin`, email `admin@admin.com`,
and password `12345`.