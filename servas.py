from flask import Flask, render_template
app = Flask(__name__)

# import render tempalte to render static files which shall be in templates folder
# for other statics as images or video files shall be in static folder also might be in subfolders with path designated.
# Note CSS file also has to be in statics


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) # debug on
