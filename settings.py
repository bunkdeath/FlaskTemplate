import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DEBUG_TB_INTERCEPT_REDIRECTS = True
# DEBUG_TB_PANELS = (
#    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
#    'flask_debugtoolbar.panels.logger.LoggingPanel',
#    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
# )
# DEBUG_TB_HOSTS = ('127.0.0.1', '::1' )
SECRET_KEY = ''
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/database.db' % BASE_DIR
SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    from settings_local import *
except:
    pass
