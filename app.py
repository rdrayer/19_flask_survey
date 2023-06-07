from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension 

app = Flask(__name__)


def test():
    '''
    Create a new virtual environment and activate it.

    Install Flask and the Flask Debug Toolbar.

    Make your project a Git repository, 
    and add ***venv/*** and ***__pycache__*** to a
    new ***.gitignore*** file for your repository.
    
    '''