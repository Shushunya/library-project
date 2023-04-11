from django.urls import path
from .views import AuthorList, AuthorDetail

app_name = 'author'
urlpatterns = [
    path("", AuthorList.as_view(), name="list-view"),
    path("<int:pk>", AuthorDetail.as_view(), name="detail-view"),
]