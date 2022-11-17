from django.urls import path

from .views import MovieList, MovieDetail, RecordList, RecordDetail
from drf_project.views import homepage


urlpatterns = [
    path("api/movies/", MovieList.as_view()),
    path("api/movies/<int:pk>/", MovieDetail.as_view()),
    path("api/records/", RecordList.as_view()),
    path("api/records/<int:pk>/", RecordDetail.as_view()),
    path('/homepage/', homepage, name='homepage'),
]
