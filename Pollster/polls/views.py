from django.shortcuts import render
from .models import Questions, Choice

# Create your views here.
def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def details(request):
    return render(request, 'polls/details.html')