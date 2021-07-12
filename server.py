from flask import Flask, render_template, request, redirect, session
from random import randint
app=Flask(__name__)
app.secret_key='Yarhar fiddledeedee'

@app.route('/')
def mainPage():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
    temp=request.form
    session['name']=temp['nameInput']
    session['location']=temp['dojoLocat']
    session['favLang']=temp['favLang']
    session['comment']=temp['comments']
    return redirect('/result')
@app.route('/result')
def result():
    return render_template('results.html')
if __name__=='__main__':
    app.run(debug=True)