from django.urls import path
from .views import *

urlpatterns = [
    path('collection/songs/<int:id>', SongDetail.as_view(), name = "SongDetail"),
    path('collection/albums/<int:id>', AlbumDetail.as_view(), name = "AlbumDetail"),
    path('collection/author/<int:id>', AuthorDetail.as_view(), name = "AuthorDetail"),
    path('collection/country/<str:country_name>', CountryDetail.as_view(), name = "CountryDetail"),
    path('collection/format/<str:format_name>', FormatTypeDetail.as_view(), name = "FormatTypeDetail"),
    path('collection/playlist/<int:id>', PlaylistDetail.as_view(), name = "PlaylistDetail"),
    path('collection/genre/<str:genre_name>', GenreDetail.as_view(), name = "GenreDetail"),
    path('collection/songs/', SongList.as_view(), name = "SongList"),
    path('collection/albums/', AlbumList.as_view(), name = "AlbumList"),
    path('collection/author/', AuthorList.as_view(), name = "AuthorList"),
    path('collection/country/', CountryList.as_view(), name = "CountryList"),
    path('collection/format/', FormatTypeList.as_view(), name = "FormatTypeList"),
    path('collection/playlist/', PlaylistList.as_view(), name = "PlaylistList"),
    path('collection/genre/', GenreList.as_view(), name = "GenreList"),
]