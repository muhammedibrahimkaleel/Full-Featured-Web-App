from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello world, You are at the polls index")


def detail(request, question_id):
    return HttpResponse("you are looking at question %s." % question_id)


def results(request, question_id):
    response = "you are looking at question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on question %s." % question_id)