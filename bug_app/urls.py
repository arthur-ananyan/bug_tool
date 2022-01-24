from django.urls import path
from .views import BugView, CommentView

urlpatterns = [

    path('bug/', BugView.as_view()),
    path('bug/<int:pk>/', BugView.as_view()),
    path('comment/', CommentView.as_view()),
    path('comment/<int:pk>/', CommentView.as_view()),
]
