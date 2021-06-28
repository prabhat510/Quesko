from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from questions.api import views as qv


router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),

    # answer a particular question
    path("questions/<slug:slug>/answer/",
         qv.AnswerCreateAPIView.as_view(), name="answer-create"),

    # displays all the answers for a particular question
    path("questions/<slug:slug>/answers/",
         qv.QuestionAnswerListAPIView.as_view(), name="answer-list"),

    path("answers/<int:pk>/",
         qv.AnswerRUDAPIView.as_view(), name="answer-detail"),

    path("answers/<int:pk>/like/",
         qv.AnswerLikeAPIView.as_view(), name="answer-like"),
]
