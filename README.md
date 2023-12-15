# Django Movie List API

# API Features:
1. List the available media streaming services Eg: Netflix, Amazon Prime Video etc
2. Registration and login
3. Add, Delete, Update movies in to the streaming service
4. Add reviews to the particular movie
5. View ratings of the movie

# Installation Process

1. Clone this repository (use `https://github.com/Naveen-arikela/MovieList-DjangoAPI.git`)

### setting up a development environment
2. start an environment with requirements
   e.g. pipenv install -r requirements.txt

### migrating the already defined models and creating the super user
3. python manage.py migrate

### super user should be created before the dummy data be loaded!
4. python manage.py createsuperuser

### run the server
4. python manage.py runserver
