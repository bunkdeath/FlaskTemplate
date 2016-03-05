# FlaskTemplate
This is a simple project in Flask to create modular application.

### Proposed directory structure
````
root_dir/
|
└ app/
|  └ module_one/
|  |  └ __init__.py
|  |  └ controller.py
|  |  └ templates/
|  |     └ index.html
|  |     └ create.html
|  |     └ ...
|  |
|  └ module_two/
|  |  └ __init__.py
|  |  └ controller.py
|  |  └ templates/
|  |     └ index.html
|  |     └ create.html
|  |     └ ...
|  |
|  └ templates
|  |  └ base.html
````

This way one can make a modular application in Flask. Each module will be independent to other in directory content. However it will use the base template of the project.

### Creating new application
```sh
$ ./manage.py startapp <appname>
```
This will create required folder structure with **_CRUD_** operation functions. Also the the blueprint for this module will be added to application.py file.

### Installation
Clone this repo to your local storage
```sh
$ git clone git@github.com:bunkdeath/FlaskTemplate.git <projectname>
$ cd <projectname>
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Running project
Clone this repo to your local storage
```sh
$ ./manage.py runserver
```

I suggest you to create virtual environment, if you haven't already used, for your project to prevent packages clash and eventually breaking already present projects.

### Home URL
This entry will soon be updated for further community discussion.