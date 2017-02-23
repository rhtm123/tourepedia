# tourepedia

Getting Started
---------------

### Initial Setup ###
1. Make a new virtualenv: ``virtualenv env``
2. Activate the virtualenv: ``source env/bin/activate``
3. Install Django & other requirements: ``pip install -r requirements.txt``


# Note: mysql database are used in this project. If you are want use basic python database then make some changes in your settings.py file as following-
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

4. Make Migrations - ``python manage.py migrate``
5. Run the server: ``python manage.py runserver``
