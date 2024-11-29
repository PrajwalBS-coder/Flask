from flask import Flask,render_template

ApplicationInstance=Flask(__name__)


@ApplicationInstance.route('/first')
def first():
    return 'It Is What It Is'

@ApplicationInstance.route('/html')
def html():
    return render_template('one.html')

@ApplicationInstance.route('/jai/<data>/')
def jai(data):
    return f'jai {data}'

@ApplicationInstance.route('/staticimg')
def staticimg():
    return render_template('staticimg.html') 


ApplicationInstance.run(debug=True,host='192.168.219.157',port=5001)
