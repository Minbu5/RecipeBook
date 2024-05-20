from flask import Flask, render_template
import requests

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


if __name__ == "__main__":
    app.run(debug=True) # debug on
