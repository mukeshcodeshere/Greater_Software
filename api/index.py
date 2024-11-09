from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
            static_folder='../static',
            template_folder='../templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)