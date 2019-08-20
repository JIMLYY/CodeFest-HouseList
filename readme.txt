
pipenv install django
Pipenv shell
pipenv install django-imagekit
pipenv install pillow

If you want to access to admin 
You should run python manage.py runserver
You should visit https://127.0.0.1:8000/admin
The user and password are 
user : HouseList
password : 2019code


if you want to create a superuser in command line run:

Python manage.py createsuperuser

)

To insert login credentials to db run below:
Mongo
Use AggieHouseList
db.cred.insert({'GOOGLE_CLIENT_ID':'970231480726-ee6ugagi5a56341q522f1s3hm2gbi2pp.apps.googleusercontent.com','GOOGLE_CLIENT_SECRET':'8xAgRAjptBOANZ_7lyueVuyv'})

