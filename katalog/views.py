from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.

def show_katalog(request):
    Data_Catalog = CatalogItem.objects.all()
    context = {
        'nama': 'Fernando Nathaniel Sutanto',
        'npm' : '2106629995',
        'all_Catalog': Data_Catalog,
        
    }
    return render(request, "katalog.html", context)
