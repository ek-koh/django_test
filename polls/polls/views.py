from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Question
from rest_framework.generics import ListCreateAPIView
from .serializers import QuestionSerializer

class ApiQuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Create your views here.
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class PollsDetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'





# def index(request):
#     a = Question.objects.order_by('-pub_date')
#     context = {"latest_question_list": a}
#     return render(request, 'polls/index.html', context)
#     # 템플릿 적용 전 코드
#     # output = ""
#     # for question in Question.objects.order_by('-pub_date'):
#     #     output += "<a href=\"/polls/" + str(question.id) + "\">" + question.question_text + "</a><br>"
#     # return HttpResponse(output)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # choice_list = get_list_or_404(question.choice_set)
#     # output = "<h1>" + question.question_text + "투표 상세화면입니다." + "<h1><br>"
#     # output += "<form action=\"/polls/" + str(question_id) + "/vote\" method=\"post\">"
#     # for choice in choice_list:
#     #     output += '<input type="radio" name="choice" value="' + str(choice.id) + '">' + choice.choice_text + "</input><br>"
#     # output += '<input type="submit" value="투표"/>'
#     # output += "</form>"
#
#     return HttpResponse(output)
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # choice_list = get_list_or_404(question.choice_set)
#
#     # output = "<h1>" + question.question_text + "<h1><br>"
#     # for choice in choice_list:
#     #     output += choice.choice_text + ":" + str(choice.votes) + "<br>"
#     #
#     return HttpResponse(output)
#
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = question.choice_set.get(pk=request.POST['choice'])

    choice.votes += 1
    choice.save()

    return HttpResponseRedirect('result')