from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import WordProcess, QueryProcessing
from . import doc
# Create your views here.
# from azlyrics import artists, songs, artists


processedDoc = WordProcess.WordProcess()
queryProcessing = QueryProcessing.QueryProcessing(processedDoc.processed_doc)
songs = doc.getLyrics()
# print(songs("Aaliyah"))

def home(request):
    return render(request, 'search/home.html')

def search(request):

    if 'keyword' not in request.GET:
        return HttpResponseRedirect("/")

    search_query = request.GET['keyword']
    processed_query = processedDoc.processString(search_query)
    result = queryProcessing.query(processed_query)

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

    id = request.GET['id']

    print(id)