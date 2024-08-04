from flask import Flask, request, render_template
from stories import stories
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
@app.route('/')
def go_home():
  """home page including a list of stories to choose from"""
  return render_template("home.html", stories = stories.stories)

@app.route('/story_form')
def story_form():
  """shows form for madlibs"""
  story_num = request.args["story_num"]
  story = stories.stories[int(story_num)]
  prompts = story.prompts
  return render_template("story_form.html",
                         prompts = prompts,
                         story_num = story_num,
                         title = story.title)

@app.route('/story')
def show_story():
  """show complete story"""
  story_num = request.args["story_num"]
  story = stories.stories[int(story_num)]
  madlib = story.generate(request.args)
  return render_template("story.html", 
                         madlib = madlib,
                         title = story.title)