from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Album,Author,FormatType,Country,Genre,Playlist,Song


class AlbumList(ListView):
    model = Album
    template_name = 'collections/collections_base.html'
    paginate_by = 10

class AuthorList(ListView):
    model = Author
    template_name = 'collections/collections_base.html'
    paginate_by = 10

class FormatTypeList(ListView):
    model = FormatType
    template_name = 'collections/collections_base.html'


class CountryList(ListView):
    model = Country
    template_name = 'collections/collections_base.html'
    paginate_by = 10


class GenreList(ListView):
    model = Genre
    template_name = 'collections/collections_base.html'
    paginate_by = 10

class PlaylistList(ListView):
    model = Playlist
    template_name = 'collections/collections_base.html'
    paginate_by = 10

class SongList(ListView):
    model = Song
    template_name = 'collections/collections_base.html'
    paginate_by = 10


class AlbumDetail(DetailView):
    model = Album
    template_name = 'collections/detail_collection.html'

class AuthorDetail(DetailView):
    model = Author
    template_name = 'collections/detail_collection.html'

class FormatTypeDetail(DetailView):
    model = FormatType
    template_name = 'collections/detail_collection.html'

class CountryDetail(DetailView):
    model = Country
    template_name = 'collections/detail_collection.html'

class GenreDetail(DetailView):
    model = Genre
    template_name = 'collections/detail_collection.html'

class PlaylistDetail(DetailView):
    model = Playlist
    template_name = 'collections/detail_collection.html'

class SongDetail(DetailView):
    model = Song
    template_name = 'collections/detail_collection.html'