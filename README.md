# Stocks API

Welcome to Stocks API! An API project that runs in Docker ecosystem using [Django REST Framework](https://www.django-rest-framework.org/) about a stocks application that lets you check your favourite financial asset price, get an asset recommendation or create your own portfolio to check its value.

[![docker](https://img.shields.io/badge/docker-blue)](https://github.com/PyCQA/python)
[![language: python](https://img.shields.io/badge/lenguage-python-blue)](https://github.com/PyCQA/python)
[![framework: django](https://img.shields.io/badge/framework-django-darkgreen)](https://github.com/topics/python)
[![package: rest framework](https://img.shields.io/badge/djangorestframework-darkred)](https://github.com/encode/django-rest-framework)

## Why Django?

Django is a Python web development framework. It is between the most used/recognized Python frameworks alongside Flask and FastAPI.
Some of the pro's of using Django are constant developer errors feedback, simplicity, pre solved problems, integrated admin site, user system, automated testing, extensive documentation, 
REST Framework also allow Django to become a backend server capable of connecting with any frontend framework and language as it is the trend in the industry nowadays. JavaScript dominates the frontend, his more popular frameworks are Vue, Angular and React.
Some of the most popular django apps are Instagram, Spotify, YouTube, Dropbox, Pinterest and many more.

## Features

Some of the features that the project contains:

- Check any ticker price
- Get an asset recommendation
- Create your own porfolio
- Add your own stocks and get daily value update!

## What's missing

- Better user authentication system.
- A real customized recommendation, a price to earnings recommendation, etc.

## Quick start

How to section with the steps to set up the project in your system.

<details><summary><b>Setting the project up</b></summary>

### Install dependencies

To run this project you need to install `Docker` and `Docker Compose`.

You can read the official documentation of [Docker](https://docs.docker.com/get-docker/) and also that of [Docker Compose](https://docs.docker.com/compose/install/).

Continue with downloading the code when you have the dependencies installed and working.

### Download the code

To download the code, the best thing to do is to `fork` this project to your personal account by clicking on [this link](https://github.com/PabloMarelli/emotive-challenge/fork). Once you have the fork to your account, download it from the terminal with this command (remember to put your username in the link):

```
git clone https://github.com/$YOUR_GITHUB_USER/emotive-challenge.git
```

> In case you don't have a Github account, or you don't want to fork, you can directly clone this repo with the command `git clone https://github.com/PabloMareli/emotive-challenge.git`.


### Initial project configuration

To run the application you need to use `docker compose up`. It will start downloading the images and creating the containers.

With the database running, it is necessary to create the tables that the application needs to work with the command `docker compose run app python3 manage.py migrate`.

It is possible to load sample data to test the API as quickly as possible. The sample data is in the `.sample_data` directory. The command needed for load fixture is as follows (in the example, the `sample_data.json` will be loaded):

```
docker compose run app python manage.py loaddata .sample_data/sample_data.json
```

### Run the application

With the initial configurations done, now it's time to run the API service with the command `docker compose up` (if you want to run the service in background, you can add the -d flag during execution). When the service starts, you can access the `Stocks API` from the browser by entering the [api root endpoint](http://localhost:8000/).

If you are able to access the `Stocks API`, it means that the application is running correctly.

</details>

## Documentation

In this section you will find the information to understand and configure the project.

<details><summary><b>See the details</b></summary>

### Main features

Below you can see the main features of the project:

* REST API endpoints with Open API docs 
* User registration and login
* Application administration panel
* Extensive usage documentation

The feature related to each application is included in the [Applications](#applications) section.

### Django Configuration

In the file `./core/settings.py` you will find the general configuration of the Django project. Within this file, all kinds of Django configurations can be made, in which the following stand out:

* Selection and configuration of the database engine.
* Applications installed within the project.
* Time zone setting.
* Project debug configuration.
* Django REST Framework specific configuration.
* Template configuration.
* Directory configuration for static files.
* User Authentication & Authorization.

For more information on all the possible configurations, you can access the official documentation at [this link](https://docs.djangoproject.com/en/4.2/topics/settings/).


### How to use the service API

The starting point of using the API is accessing its [root](http://localhost:8000) via a browser. From there you can see some useful endpoints related to user registration, login and the rest of the application endpoints.

**User Registration & Login**

1. Access to the [root endpoint](http://localhost:8000) to explore the service endpoints.
2. Access to the [user registration](http://localhost:8000/users/signup) endpoint to create an user account. Fill fields with your username, email and a strong password.
3. Access to the [user login](http://localhost:8000/users/login) and insert your email and password. An access tokens will be returned. You can save it for your mobile/web/desktop app. If you are using the Open API docs the user will be logged in.
4. Go to [root endpoint](http://localhost:8000) and explore applications endpoints.

**User Logout**

To logout just follow the [user logout](http://localhost:8000/users/logout) endpoint and send a POST request.

**Applications flows**

The specific app endpoints are described in each section of [Applications](#applications).

### Using the admin site

The API service has an integrated administration panel that allows you to perform CRUD operations on each of registered applications models (tables). To use the admin site you must create a superuser before. Execute the command `docker compose run app python manage.py createsuperuser`, enter your email and your password twice and then go to [admin endpoint](http://localhost:8000/admin) to login with your credentials.

Apart of the base sections, there are the custom applications, explained in the [Applications](#applications) section.


### Database manipulation

Django provides an excellent database manipulation without the need to use any external tools to perform the necessary operations.

If you want to make a simple backup of the database, execute the following command:

```
docker compose run app \
python3 manage.py dumpdata --indent 2 > .fixtures/db.json
```

If you want to make a backup of the database that can be used in a fresh database, execute the following command:

```
docker compose run app \
python3 manage.py dumpdata --indent 2 \
--exclude auth.permission --exclude contenttypes --exclude admin.logentry > .fixtures/db.json
```

To load the application data into a fresh database, run the following command to create the necessary tables:

```
docker compose run app python manage.py migrate
```

And then load data inside the tables:

```
docker compose run app python manage.py loaddata .fixtures/db.json
```

## Applications 📚

In this section you will find information that will help you to have a greater context about each custom applications.

<details><summary><b>Read the apps info</b></summary>

### Stocks API

The stocks API manages portfolio, stocks, ticker price and recommend asset.

<details><summary><b>See all info related to Stocks API</b></summary>

#### Sample data

The application comes with sample data ready to load at `.sample_data/sample_data.json`. To load this data you have to execute the command `docker compose run app python manage.py migrate` and then, execute the command `docker compose run app python manage.py loaddata .sample_data/sample_data.json` as explained in [Quick Start](#quick-start) section.

#### Using the admin site

At first, it is necessary to create a superuser as described in the [Using the admin site](#using-the-admin-site) and then, login at the [admin endpoint](http://localhost:8000/admin). 

Inside the admin panel you can create different assesments, assign questions and options. From the left panel you can create all the entities that you consider necessary and the relationships between them.


#### Endpoints

Each endpoint is listed below, with its description and available methods.

* `/` - Shows a list with all the available resources of the application (GET)
* `stocks/ticker/<str:ticker>` - Retrieve the price of a ticker (GET)
* `stocks/recommend/` - Recommends a financial asset (GET)
* `stocks/<int:pk>/` - Shows the detail of a Stock object (GET)
* `stocks/add/<int:pk>/` - Adds a Stock object (POST)
* `stocks/update/<int:pk>/` - Updates a Stock object (POST)
* `stocks/delete/<int:pk>/` - Deletes a Stock object (POST)
* `stocks/portfolio/` - List all Portfolio object for the logged user (GET)
* `stocks/portfolio/<int:pk>/` - Shows the detail of Portfolio object (GET)
* `stocks/portfolio/add/<int:pk>/` - Adds a Portfolio object (POST)
* `stocks/portfolio/update/<int:pk>/` - Updates a Portfolio object (POST)
* `stocks/portfolio/delete/<int:pk>/` - Deletes a Portfolio object (POST)

</details>

## User

The user app manages authorization, registration, password, login.

<details><summary><b>See all info related to User API</b></summary>

### User authorization endpoints

The response from the endpoint returns the id and URL of the created instance. With that id you can access the following endpoints:

* `users/login/`: returns token key. (POST)
    username,
    password
* `users/test-token/`: returns JSON object.
    token
* `users/profile/`: returns JSON object.
    token

### Registration endpoints

* `users/registration/`: registration endpoint. (POST)
    username
    password
    email

</details>

</details>

## Used technologies 🛠️

In this section you can see the most important technologies used.

<details><summary><b>See the complete list of technologies</b></summary><br>

* [Docker](https://www.docker.com/) - Ecosystem that allows the execution of software containers.
* [Docker Compose](https://docs.docker.com/compose/) - Tool that allows managing multiple Docker containers.
* [Python](https://www.python.org/) - Language in which the services are made.
* [Django](https://www.djangoproject.com/) - Popular Python framework for web application development.
* [Django REST Framework](https://www.django-rest-framework.org/) - Django-based framework for designing REST APIs.
* [PostgreSQL](https://www.postgresql.org/) - Database to query and store data.
* [Visual Studio Code](https://code.visualstudio.com/) - Popular multi-platform development IDE.

</details>

## About me 

Hi, I’m Pablo, hope youre doing great! Im a 3+YOE Python backend engineer, quick learner, tenacious problem solver and results deliverer. Proficient in spoken and written english. All my experience is using the following tech stack, Python, Django and MySQL. Develop and design of REST APIs using MVC/MVT architecture, integration APIs and objects/database management panels/dashboards overriding and customizing Django admin. Database, models and relationship design. Also a little bit of frontend with HTML, CSS and JavaScript. NodeJS. Docker. Git and GitHub. Linux. CI/CD GitHub Actions. AWS cloud, EC2, ECS, PS, S3, Lambdas.
