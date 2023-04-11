from django.urls import path
from .views import BookList, BookDetail, BookSeriesList, BookSeriesDetail

app_name = 'book'
urlpatterns = [
    path("", BookList.as_view(), name="list-view"),
    path("<int:pk>", BookDetail.as_view(), name="detail-view"),
    path("series/", BookSeriesList.as_view(), name="series-list"),
    path("series/<int:pk>", BookSeriesDetail.as_view(), name="series-detail"),
]
