from django.shortcuts import render,get_object_or_404,redirect
from .forms import ImageForm
from .models import Image
from django.http import Http404


# Create your views here.
def home(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=ImageForm()
    img=Image.objects.all()
    return render(request,'imageapp/home.html',{'img':img,'form':form})


def details(request, id):
    image = get_object_or_404(Image, id=id)
    return render(request, 'imageapp/details.html', {'img': image})

def delete_image(request, id):
    image = get_object_or_404(Image, id=id)
    if request.method == "POST":
        image.delete()
        return redirect('home')
    return redirect('details')