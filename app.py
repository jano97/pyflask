from flask import Flask, render_template, request, url_for, redirect, jsonify
import json
import os.path


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
app.secret_key = 'ngwrj86w63ergw63'



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/branding')
def branding():
    return render_template('branding.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        with open('file.json', 'a') as f:
            json.dump(request.form, f)
        return render_template('contact.html')
    else:
        return render_template('contact.html')

@app.route('/frindex')
def frindex():
    return render_template('frindex.html')

@app.route('/frworks')
def frworks():
    return render_template('frworks.html')

@app.route('/frbranding')
def frbranding():
    return render_template('frbranding.html')

@app.route('/frfaq')
def frfaq():
    return render_template('frfaq.html')

@app.route('/frcontact')
def frcontact():
    return render_template('frcontact.html')

if __name__== '__main__':
    db.create_all()
    app.run(debug=True)
