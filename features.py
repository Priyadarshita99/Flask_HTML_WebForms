from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField

FAI=Flask(__name__)

@FAI.route('/htmlform',methods=['GET','POST'])
def htmlform():
    if request.method=='POST':
        FD=request.form
        username=FD['un']
        return username
    return render_template('htmlform.html')

class NameForm(Form):
    firstname=StringField()
    lastname=StringField()
    submit=SubmitField()

@FAI.route('/webform',methods=['GET','POST'])
def webform():
    NFO=NameForm()
    if request.method=='POST':
        NFDO=NameForm(request.form)
        if NFDO.validate():
            return NFDO.firstname.data
    return render_template('webform.html',NFO=NFO)     

if __name__=='__main__':
    FAI.run(debug=True,host='192.168.1.8',port=5001)
    