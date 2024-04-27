from flask import Flask
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

if __name__ == '__main__':
    app.run()
