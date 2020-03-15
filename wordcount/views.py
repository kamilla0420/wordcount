from django.http import HttpResponse 
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'date':'2020.03.13.'})
    
def count(request):
    fulltext = request.GET['count']
    
    words = fulltext.split()
    worddictionary = {}
    
    for word in words:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
            
    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(words), 'wordd': sortedWords})
	
def about(request):

	name="Kamilla Kiss"
	
	return render(request, 'about.html', {'name': name})
    