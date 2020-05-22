from flask import Flask

app = Flask("project")
app.secret_key = "Killer2391998"

from project.controllers import *
