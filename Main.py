from flask import Flask, render_template,jsonify
#from flask-ngrok import run_with_ngrok
app = Flask(__name__) #This is how flask determines how to import files and modules into app

@app.route('/')
def index():
    return '<H1>Hello World!</H1><p>Under Construction</p>'
@app.route('/about')
def about():
    return 'About Me'

@app.route('/contact/<name>/<price>')
def contact(name,price):
    return f'<H1>{name}</H1><p>Contact: {price}</p>'

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', name=username)

@app.route('/first-template')
def first_template():
    return render_template('first_template.html', name='PyCharm')

Courses = [
    {'id': 1,
     'title': 'Hello Coding',
     'image_url' : 'https://s3.amazonaws.com/creare-websites-wpms-legacy/wp-content/uploads/sites/32/2016/03/01200959/canstockphoto22402523-arcos-creator.com_-1024x1024.jpg',
     'id': 2,
     'title': 'Machine Learning for Everybody',
     'image_url': 'https://cdn01.dailycaller.com/wp-content/uploads/2019/06/Test-Shutterstock.jpg',
     'id': 3,
     'title': 'Wall Street Coder',
     'image_url': 'https://www.technibble.com/articlecontent/2008/06/monitortester2.jpg'}
]


@app.route('/api/courses')
def api_courses():
    return jsonify(Courses)

@app.route('/courses')
def courses():
    return render_template('all_courses.html', courses=Courses)

if __name__ == '__main__':
    app.run()
