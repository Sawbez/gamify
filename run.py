from sys import argv

from templates import app

if len(argv) > 1 and argv[1] == "prod":
    app.config.from_object("configurations.ProductionConfig")
else:
    app.config.from_object("configurations.DevelopmentConfig")

app.run()
