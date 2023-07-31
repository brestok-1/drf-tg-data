# <div align="center">BOOKS API DATA🔎</div>

<div align="center">
<img src="assets/book_data.png" align="center" style="width: 100%; height: 40%" />
</div>

## Description

This project was created with the aim of providing API data for
my [telegram bot](https://github.com/brestok-1/book-tg-bot), updating data, adding new books. It is
very simple in its structure, but its creation has improved my API integration and data parsing
skills. [The project was deployed on pythonanywhere](http://booktgbotapi.pythonanywhere.com/api/books/).

## Technologies

***Language***

![Python](https://img.shields.io/badge/-Python-1C1C1C?&style=for-the-badge)

***Framework***

![Django](https://img.shields.io/badge/-Django-1C1C1C?&style=for-the-badge)

***Databases***

![Postgres](https://img.shields.io/badge/-Postgresql-1C1C1C?&style=for-the-badge)
![SQLite](https://img.shields.io/badge/-SQLite-1C1C1C?&style=for-the-badge)

***Libraries***

![DRF](https://img.shields.io/badge/-DRF-1C1C1C?&style=for-the-badge)
![Psycopg2-binary](https://img.shields.io/badge/-psycopg2-1C1C1C?&style=for-the-badge)

***Other***

![Docker](https://img.shields.io/badge/-Docker-1C1C1C?&style=for-the-badge)

The project is very simple in its structure: it has a book model and an author model. I made a readonly permission. New
books can only be added via the Django-admin panel. I used the Django Rest Framework library to convert python objects
to json data.

## Project setup

***Method 1: Via docker-compose***

1. Create a .env file and paste the data from the .env.example file into it
2. The value of the variable ALLOWED_HOST specify 'localhost'
3. Generate django secret key on [this site](https://djecrety.ir/) and specify it in the SECRET_KEY variable
4. In the terminal, enter the following command:

```
docker-compose up -d --build
```

5. Perform migration to the database:

```
docker-compose exec web python manage.py migrate
```

6. Create a superuser by entering the following command:

```
docker-compose exec web python manage.py createsuperuser
```

7. Log in to the [admin panel](http://127.0.0.1:8000/admin) using the data of the superuser you created and add several books

***Method 2: Via virtual environment***

1. Create and activate a python virtual environment
2. In the terminal, enter the following command:

```
pip3 install -r requirements.txt
```

3. Create a .env file and paste the data from the .env.example file into it
4. The value of the variable ALLOWED_HOST specify 'localhost'
5. Generate django secret key on [this site](https://djecrety.ir/) and specify it in the SECRET_KEY variable
7. In the book_tg_api/settings file.py in the DATABASE variable, specify the following value:

```
{
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
8. Perform migration to the database:

```
python manage.py migrate
```

9. Create a superuser by entering the following command:

```
python manage.py createsuperuser
```

10. In the terminal, enter the following command:

```
python manage.py runserver
```

11. Log in to the [admin panel](http://127.0.0.1:8000/admin) using the data of the superuser you created and add several books

#### Use this project together with [telegram bot](https://github.com/brestok-1/book-tg-bot) to add your books. To do this, in the telegram bot project in external_services/book_api.py in the _get_api_data function, replace the reference with
```
http://127.0.0.1:8000/api/books
```
## <div align="center">Enjoyable to use!👋</div>