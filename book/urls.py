from django.urls import path
from .views import BookList, BookDetail

app_name = 'book'
urlpatterns = [
    path("", BookList.as_view(), name="list-view"),
    path("<int:pk>", BookDetail.as_view(), name="detail-view"),
]