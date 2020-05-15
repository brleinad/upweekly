# UpWeekly

**UpWeekly** is a web application to track tasks on a weekly basis and automate performance reviews.

## Introduction
Throughout my career I have constantly kept a weekly journal were I would write down what I got done that week and my plans for the following week.
Then for my yearly performance review report I would simply have to copy the highlights from my weekly journal.
I started a journal every year and every year it helped a lot for these reports.
This app is based on my experience using a journal while adding some extra automation.
It is being developed using Python and Django.

## Trying It Out
At the moment the app is deployed on Heroku at [https://upweekly.herokuapp.com/](upweekly.herokuapp.com) but it's still using SQLite and I will probably deploy on AWS using PostGreSQL in a near future.

## How To Set Up a Development Environment
You will need Python 3.7 or higher installed.
Clone or fork the repo, go into  the project directory and then it's just a matter of setting up pipenv.
```
pipenv install
pipenv shell
```
After that you can run a local server:
```
python manage.py runserver
```
