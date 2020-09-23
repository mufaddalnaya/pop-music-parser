from django.shortcuts import render
from django.http import HttpResponse
from . import WordProcess, QueryProcessing
# Create your views here.

processedDoc = WordProcess.WordProcess()
queryProcessing = QueryProcessing.QueryProcessing(processedDoc.processed_doc)

def home(request):
    return render(request, 'search/home.html')

def search(request):

    search_query = request.GET['keyword']
    processed_query = processedDoc.processString(search_query)
    result = queryProcessing.query(processed_query)
    context = {
        'documents':result,
        'search_query':search_query,
        'totalDocs': len(result)
    }

    return render(request, 'search/search.html', context)