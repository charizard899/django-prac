from django.http import HttpResponse
from django.shortcuts import render

data={
    'movies': [
        {
            'id': 5,
            'title': 'The Shawshank Redemption',
            'year': 1669
        },
        {
            'id': 6,
            'title': 'The Godfather',
            'year': 1779
        },
        {
            'id': 7,
            'title': 'The Dark Knight',
            'year': 1889
        }
    
    ]
}

def movies(request):
    #return HttpResponse("Hello there")
    return render(request, 'movies/movies.html', data)


def home(request):
    return HttpResponse("Home Page")