## What Is It

The codebase for the iggmarathon.com 2016 site rewrite. (At the time of writing this README, I'm uploading what I've built so far so we can have a framework to start building and collaborating on.)

## Getting Started
First, make sure you have Python 2. If you're not on Windows, you probably already have it.

Next, you'll probably want to set up a virtual environment so you don't pollute your global libraries. There are many ways to go about this; I really like [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/index.html) and `mkvirtualenv`.

Got that working? Install all of the libraries: `pip install -r requirements.txt`. (Incidentally, if you need to add a library to the project in the future, that's where it goes.)

Yay, now you have libraries! We do all our database stuff with Alembic, which probably deserves its own little section, so:

## Alembic and Actually Running Things
TL;DR: `alembic upgrade head`, `./manage.py prepopulate`

If you haven't done anything else, first you'll need to actually make your database.

`alembic upgrade head` updates your database schema to the latest version. Run this any time the schema gets updated, and Alembic will handle adding and dropping tables and columns.

Have a current database schema? You can do a few things from here: `./manage.py prepopulate` adds some sample data to the database. Wanna change what sample data that is? Modify `prepopulate_database()` in `src/data/prepopulate.py`.

Want to make schema changes? `alembic revision -m 'descriptive message about the change'`, then modify the file that Alembic creates to make your changes.

Want to just run the server? `./manage.py runserver`, visit `localhost:5000` in your browser of choice.

## Structural Overview
- All of the models are, predictably, in `data/models`. To make a new Foo and save it to the database: `Foo.create(...)`
- All of the HTML is in `web/templates`. Flask is opinionated about its templating and expects [jinja2](http://jinja.pocoo.org/docs/dev/).
- Route implementations are in `web/views`. The actual wiring of the routes happens in `web/routes.py`, should you want to add a new route.
- Configuration is in `settings.py`. You can read any setting by importing app_config from settings, which is just a dictionary of every config option. _DO NOT ADD PRIVATE KEYS OR PASSWORDS TO THINGS TO THIS FILE, THAT WOULD BE VERY SAD_.
