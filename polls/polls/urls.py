from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.PollsDetailView.as_view(), name='detail'),
    path('<int:pk>/result', views.ResultView.as_view(), name='result'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('api', views.ApiQuestionList.as_view(), name='api')
]
