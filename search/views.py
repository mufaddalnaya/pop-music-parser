from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import WordProcess, QueryProcessing
from . import doc

processedDoc = WordProcess.WordProcess()
queryProcessing = QueryProcessing.QueryProcessing(processedDoc.processed_doc)
songs = doc.getLyrics()
total_clicks = 0
song_clicks = [0]*100
trending_this_week = [[0]*100]*7

def home(request):
    trending_list = trending()
    trending_tracks = []
    for i in range(5):
        trending_tracks.append(songs[trending_list[i]])
    context = {
        'trending_tracks':trending_tracks
    }    
    # print(trending_list[0:10])
    # print(song_clicks)
    return render(request, 'search/home.html', context)

def search(request):

    if 'keyword' not in request.GET:
        return HttpResponseRedirect("/")

    search_query = request.GET['keyword']
    processed_query = processedDoc.processString(search_query)
    result = queryProcessing.query(processed_query, total_clicks, song_clicks)

    for lyrics in result:
        lyrics['title'] = songs[lyrics['id']]['title']
        lyrics['artist'] = songs[lyrics['id']]['artist']

    context = {
        'documents':result,
        'search_query':search_query,
        'totalDocs': len(result)
    }

    return render(request, 'search/search.html', context)

def song(request):

    if 'id' not in request.GET:
        return HttpResponseRedirect("/")

    id = int(request.GET['id'])
    context = {
        'message':"Song ID Invalid"
    }
    if id not in songs:
        return render(request, 'search/error.html', context)

    song_clicks[id] = song_clicks[id]+1
    global total_clicks
    total_clicks = total_clicks+1
    # print(total_clicks)

    context = {
        'songDetails':songs[id]
    }

    return render(request, 'search/song.html', context)


def trending():
    trending = [1,22,33,43,55]

    return trending