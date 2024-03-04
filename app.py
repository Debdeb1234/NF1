# app.py

from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

def execute_attack(attack_type, url):
    command = f"python {attack_type}.py {url}"
    subprocess.run(command, shell=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        attack_type = request.form['attack_type']
        execute_attack(attack_type, url)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
