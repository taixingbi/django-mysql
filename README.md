
```
python3 -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt
```

### run migrate
##### packaging up your model changes
```
python manage.py makemigrations 
```
##### applying those to your database.
```
python manage.py migrate 
Username: test
Password: test
```

### run local
```
python manage.py runserver 0.0.0.0:8083
python manage.py createsuperuser
```
