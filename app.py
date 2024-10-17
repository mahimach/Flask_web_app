from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex = request.form['regex']
    try:
        matches = re.findall(regex, test_string)
    except re.error:
        matches = ["Invalid regex pattern"]
    return render_template('index.html', test_string = test_string, regex = regex, matches = matches)

@app.route('/valid-mail', methods=['GET','POST'])
def validate_mail():
    if request.method == 'POST':
        email = request.form['email']
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        is_valid = re.match(email_regex, email) is not None
        return render_template('emailvalidation.html', email = email, is_valid = is_valid)
    return render_template('emailvalidation.html', email=None, is_valid=None)


if __name__ == '__main__':
    app.run(debug=True)
