from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.db import connection
from .models import Quiz, questions , anskey , result

context = {
        'quiz': Quiz,
        'questions': questions,
        'anskey': anskey,
        'result': result,
    }

def quiz(request , quizname):
	quiz = questions.objects.get(inQuiz = quizname)
	return render(request, 'USER/quiz.html' , {'quiz': quiz})
	return redirect('result/{{quizname}}')

def home(request):
	return render(request, 'USER/home.html' , context )

def dashboard(request):
	return render(request, 'USER/dashboard.html' , context)

def leaderboard(request):
	return render(request, 'USER/leaderboard.html' , context)

def prevAns(request):
	return render(request, 'USER/prevAns.html' , context)

def result(request, quizname):
	quiz = questions.objects.get(inQuiz = quizname)
	context = {
        'quiz': QUIZs,
        'questions': questions,
        'anskey': anskey,
        'result': result,
        'currentQuiz': quiz,
    }
	if request.method == 'POST':
		total = 0
		for q in quiz:
			currentUser = request.user
			currentQuiz = quizname
			question = q.question
			ans = request.POST.get({{q.question}})
			ak = anskey(username=currentUser , inQuiz = currentQuiz, ofQuestion= question, givenAns=ans)
			ak.save()
			if ans == q.anskey:
				marks = 4
			else:
				marks = -1
			total += marks


			res = result(username=currentUser, inQuiz=currentQuiz, marks= marks, total= total)
			res.save()

	return render(request, 'USER/result.html' , context )


def addQuestions(request):
	totMarks=0

	if request.method == 'POST':
		qno=request.POST.get('qno')
		question=request.POST.get('question')
		inquiz=request.POST.get('inQuiz')
		opt1=request.POST.get('opt1')
		opt2=request.POST.get('opt2')
		opt3=request.POST.get('opt3')
		qtype=request.POST.get('qtype')
		anskey=request.POST.get('anskey')
		qs = questions(qno=qno, question=question, inQuiz=inquiz, opt1=opt1, opt2=opt2, opt3=opt3, qtype=qtype, anskey=anskey)
		qz = Quiz(quizName=inquiz)
		qz.save()
		qs.save()
		



	return render(request, 'USER/addQuestions.html' , context)
	return redirect('addQuestions/')

def addquiz(request):
	if request.method == 'POST':
		inquiz=request.POST.get('inQuiz')
		qz = Quiz(quizName=inquiz)
		qz.save()
		
	return render(request, 'USER/addquiz.html' , context)
