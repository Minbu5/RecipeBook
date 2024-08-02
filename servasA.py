from flask import Flask, render_template
import requests
import webbrowser
from threading import Timer

data = requests.get(url='https://api.npoint.io/e64ca40c2443ee7ed2f3').json()

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recipies/<category>')
def all_recipies(category):
    return render_template('all_recipies.html', data=data, category=category,)

@app.route('/recipe/<category>/<int:num>')
def selected_recipe(category, num):
    return render_template('recipe.html', data=data, category=category, num=num)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(port=5000)
    # app.run(debug=True) # debug on




