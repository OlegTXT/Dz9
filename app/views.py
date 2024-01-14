from django.shortcuts import render
from .models import Musician, Genre


def genre_list_view(request):
    genre = Genre.objects.all()
    context = {'genre_list': genre}

    return render(request, 'app/genre_list.html', context)


def genre_detail_view(request, pk):
    genre = Genre.objects.get(pk=pk)
    musicians = Musician.objects.filter(genre=genre)
    context = {'genre': genre, 'musicians': musicians}

    return render(request, 'app/genre_detail.html', context)


def musician_detail_view(request, pk, musician_slug):
    genre = Genre.objects.get(pk=pk)
    musician = Musician.objects.get(slug=musician_slug)
    context = {'genre': genre, 'musician': musician}

    return render(request, 'app/musician.html', context)
