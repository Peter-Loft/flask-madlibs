from click import prompt
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def show_form():
    """ 
    Takes prompts from the story instance, updates questions
    html form to reflect prompts. When submitted makes a GET 
    request with form values to the flask show_story 
    """

    prompts = silly_story.prompts
    # replace prompts inside of return statement

    return render_template("questions.html", prompts=prompts)


@app.get('/story')
def show_story():
    """ 
    Accepts dictionary-like object from show_form GET 
    request, calls generate method to produce story text.
    """

    return render_template("story.html", text=silly_story.generate(request.args))
