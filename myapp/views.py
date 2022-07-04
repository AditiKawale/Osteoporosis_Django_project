from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'myapp/base.html')

def upload(request):          #Training model
    form=ImageForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    messages.success(request,"Image uploaded successfully!!")
    form=ImageForm()
    img=Image.objects.all()
    return render(request, 'myapp/bs.html',{'img':img,'form':form})

def delete_img(request,id):
    im=Image.objects.filter(id=id)
    # if len(im.photo.path)>0:
    #     os.remove(im.photo.path)
    im.delete()
    return redirect('/upload')

def test(request):
    form=ImageForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    form=ImageForm()
    img=Image.objects.all()
    return render(request, 'myapp/test.html',{'img':img,'form':form})
