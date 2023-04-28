from flask import Flask
app=Flask(__name__)
app.secret_key="fytykjkbyr5r3565"
from app.controllers import default