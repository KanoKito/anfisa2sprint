from django.shortcuts import render
from ice_cream.models import IceCream

def index(request):
    template = 'homepage/index.html'
    
    ice_cream_list = IceCream.objects.filter(
        is_published=True,
        is_on_main=True
    ).order_by('title')[:3].values('id', 'title', 'description')
    
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)