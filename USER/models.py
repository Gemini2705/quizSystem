from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
	srno = models.IntegerField()
	quizName = models.CharField(max_length= 100, primary_key=True)
	totalMarks = models.IntegerField()

class questions(models.Model):
	qno = models.IntegerField()
	question = models.TextField(primary_key=True)
	inQuiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	opt1 = models.CharField(max_length = 50)
	opt2 = models.CharField(max_length = 50)
	opt3 = models.CharField(max_length = 50)
	qtype = models.CharField(max_length = 15) #can be MCQ , TrueFalse , Multiple
	ansKey = models.CharField(max_length = 20)

class anskey(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	inQuiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	ofQuestion = models.ForeignKey(questions, on_delete=models.CASCADE)
	givenAns = models.CharField(max_length = 20)

class result(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	inQuiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	marks = models.IntegerField()
	total = models.IntegerField()

