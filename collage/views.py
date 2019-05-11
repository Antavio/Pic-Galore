from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def index(request):
    image_catalogue = Image.all_images()
    return render(request,'collage/index.html',{"all_images":image_catalogue})

def search_images(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        search_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'collage/search.html',{"message":message,"images_searched":search_images})

    else:
        message = "You haven't searched yet"
        return render(request,"collage/search.html",{"message":message})

