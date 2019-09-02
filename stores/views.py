from django.shortcuts import render
from .models import Store
from django.http import JsonResponse
import requests

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

def store_detail(request, store_id):
    store = get_list_or_404(Store, id=store_id)
    context = {
        "store": store
    }
    return render (request, 'store_detail.html', context)

def api_test(request):
	url= "https://pokeapi.co/api/v2/pokemon/"

	nxt= request.GET.get('n')
	prv=request.GET.get('p')

	if nxt:
		response = requests.get(nxt).json()
	elif prv:
		response = requests.get(prv).json()
	else:
		response = requests.get(url).json()

	context={

		"results": response["results"],
		'next':response["next"],
		'previous':response["previous"],
	}
	return render(request, 'api.html', context)

def api_detail(request):
	url= request.GET.get('detail')
	response = requests.get(url).json()

	context={

		'r': response,
	}
	return render(request, 'api_detail.html', context)