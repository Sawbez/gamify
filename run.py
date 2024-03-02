from sys import argv

from templates import app

if argv[1] == 'prod':
    app.config.from_object('configurations.ProductionConfig')
else:
    app.config.from_object('configurations.DevelopmentConfig')

app.run()