from django.urls import path
from .views import *

urlpatterns = [
    path('collection/songs/<int:id>', SongDetail.as_view()),
    path('collection/albums/<int:id>', AlbumDetail.as_view()),
    path('collection/author/<int:id>', AuthorDetail.as_view()),
    path('collection/country/<str:country_name>', CountryDetail.as_view()),
    path('collection/format/<str:format_name>', FormatTypeDetail.as_view()),
    path('collection/playlist/<int:id>', PlaylistDetail.as_view()),
    path('collection/genre/<str:genre_name>', GenreDetail.as_view()),
    path('collection/songs/', SongList.as_view()),
    path('collection/albums/', AlbumList.as_view()),
    path('collection/author/', AuthorList.as_view()),
    path('collection/country/', CountryList.as_view()),
    path('collection/format/', FormatTypeList.as_view()),
    path('collection/playlist/', PlaylistList.as_view()),
    path('collection/genre/', GenreList.as_view()),
]