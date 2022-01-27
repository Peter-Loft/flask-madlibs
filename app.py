from click import prompt
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/templates/questions.html')
def show_form():
    prompts = silly_story.prompts 
    # replace prompts inside of return statement
    
    return render_template("questions.html", prompts = prompts)