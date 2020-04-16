#!/usr/bin/python
from flask import Flask, render_template, url_for, request, session, redirect, flash, jsonify
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import Form

#Create the app and configure it
app = Flask(__name__, template_folder='templates' , static_folder="static")

app.config["DEBUG"] = True
app.config["TESTING"] = True

app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)
SECRET_KEY='hello_bhai'
app.config['SECRET_KEY']=SECRET_KEY

class SubmitForm(Form):
	question = CKEditorField('question')

@app.route('/',methods=['GET','POST'])
def home():
	form=SubmitForm()
	if request.method=='GET':
		return render_template('index.html',form=form)
	else:
		x=form.question.data
		print (x)
		return render_template('display.html',x=x)

if __name__ == '__main__':
	app.run()
