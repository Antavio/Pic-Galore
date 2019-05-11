from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def index(request):
    image_catalogue = Image.all_images()
    return render(request,'collage/index.html',{"all_images":image_catalogue})


