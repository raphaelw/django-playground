# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    results_url_path = reverse(results, kwargs={"question_id":123})
    return HttpResponse(f"""You're looking at question {question_id}. Results: {results_url_path}""")

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
