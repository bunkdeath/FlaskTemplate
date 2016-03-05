#!/usr/bin/env python

import os
import shutil
from flask.ext.script import Manager

from application import app


manager = Manager(app)
@manager.command
def createapp(app_name):
    '''Create a new app. A name must be provided. e.g. ./app.py createapp user'''

    def move_template(app_name):
        # creating copy of apptemplate with new app name
        source = os.path.join(app.config.get('BASE_DIR'), 'apptemplate')
        destination = os.path.join(app.config.get('BASE_DIR'), 'app', app_name)
        shutil.copytree(source, destination)

        # rename template appname folder with user provided app name
        source = os.path.join(app.config.get('BASE_DIR'), 'app', app_name, 'templates', 'appname')
        destination = os.path.join(app.config.get('BASE_DIR'), 'app', app_name, 'templates', app_name)
        shutil.move(source, destination)

    def update_template_code(app_name):
        # replace 'appname' with app name provided by user in controller file
        filename = os.path.join(app.config.get('BASE_DIR'), 'app', app_name, 'controller.py')
        with open(filename) as f:
            updated_code = f.read().replace('appname', app_name)

        with open(filename, "w") as f:
            f.write(updated_code)

    def update_application(app_name):
        filename = os.path.join(app.config.get('BASE_DIR'), 'application.py')
        tmp_file = os.path.join(app.config.get('BASE_DIR'), 'application.swap')
        import_text = "from app.%s.controller import module as %s_module" % (app_name, app_name)
        blueprint_text = "app.register_blueprint(%s_module, url_prefix='/%s')" % (app_name, app_name)

        new_app = open(tmp_file, 'w')
        with open(filename, 'r+') as application:
            for line in application:
                if line.strip() == "# END Import a module":
                    new_app.write(import_text)
                    new_app.write('\n')
                elif line.strip() == "# END Register blueprints":
                    new_app.write(blueprint_text)
                    new_app.write('\n')
                new_app.write(line)

        shutil.move(tmp_file, filename)

    move_template(app_name)
    update_template_code(app_name)
    update_application(app_name)

manager.run()
