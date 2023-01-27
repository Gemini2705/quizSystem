from django import forms

class addQstn(forms.Form):
	qno = forms.IntegerField()
	question = forms.TextField()	
	opt1 = forms.CharField()
	opt2 = forms.CharField()
	opt3 = forms.CharField()
	qtype = forms.CharField() 
	ansKey = forms.CharField()



