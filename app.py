from click import prompt
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def show_landing_page():
    """ 
    Takes prompts from the story instance, updates questions
    html form to reflect prompts. When submitted makes a GET 
    request with form values to the flask show_story 
    """
    
    return render_template("dropdown.html", templates = ["silly", "excited"])

@app.get('/form')
def show_form():
    """ 
    Takes prompts from the story instance, updates questions
    html form to reflect prompts. When submitted makes a GET 
    request with form values to the flask show_story 
    """
    print(request.args)
    template = silly_story.prompts if request.args["silly"] == "silly" else excited_story.prompts
    
    return render_template("questions.html", prompts = template)


@app.get('/story')
def show_story():
    """ 
    Accepts dictionary-like object from show_form GET 
    request, calls generate method to produce story text.
    """

    return render_template("story.html", text=silly_story.generate(request.args))
