# Quesko
Quesko is a quora like question answer web application made using django, django restframework and VueJs.
#### create a python virtual environment and activate it:
```
virtualenv venv
```

#### install dependencies from requirements.txt:
```
pip install -r requirements.txt
```

#### Apply the migrations:
```
python manage.py migrate
```

#### install all the VueJs dependencies:
```
cd Quesko/frontend
npm install 
```
#### run VueJs development server:
```
npm run serve
```
#### run django development server:
```
python manage.py runserver
```

#### Now open up chrome and your project is running at 127.0.0.1:8000
