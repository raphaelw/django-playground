# from django.shortcuts import render

from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
        "page_title": "All Questions",
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # or in short: question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question, "page_title": "Question"})

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
