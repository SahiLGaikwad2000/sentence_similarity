
from crypt import methods
from nlp import similar
from flask import Flask

from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)


@app.route('/')

def home():
	return render_template('new.html')

@app.route('/detect',methods=['POST'])
def detect():
    if request.method=='POST':
        s1=request.form.get('s1')
        s2=request.form.get('s2')
        a=similar(s1,s2)
        b=float("{:.2f}".format(a))*100
        print(float(b)*100)

        return render_template('new.html',data=b,s1=s1,s2=s2)

if __name__ == '__main__':

	
	app.run()
