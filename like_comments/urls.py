from django.urls import path
from like_comments import views


urlpatterns = [
    path('liked/', views.LikedCommentList.as_view()),
    path('liked/<int:pk>/', views.LikedCommentDetail.as_view()),
]
