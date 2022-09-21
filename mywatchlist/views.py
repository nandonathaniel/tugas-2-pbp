from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_html(request):
    data_watchlist = MyWatchList.objects.all()
    deltaWatched = 0
    for movie in data_watchlist:
        if movie.watched == True:
            deltaWatched += 1
        else:
            deltaWatched -= 1
    context = {
        'list_watchlist': data_watchlist,
        'nama': 'Fernando Nathaniel Sutanto',
        'npm': '2106629995',
        'watch_many': (deltaWatched >= 0),
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_json(request):
    data_watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")