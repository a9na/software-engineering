from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse

from .models import Image, Comment

# Create your views here.
def home(request):
    formatted_time = timezone.now().strftime("%H:%M:%S.%f")
    context = {
        'current_time': formatted_time,
    }
    return render(request,  'images/home.html', context)

def index(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'images/index.html', context)

def detail(request, id):
    image = get_object_or_404(Image, pk=id)

    viewed_images = request.session.get("viewed_images", "")
    viewed_images = viewed_images.split(",")
    if str(image.id) not in viewed_images:
        image.views += 1
        image.save()
        viewed_images.append(str(image.id))
        request.session['viewed_images'] = ",".join(viewed_images)
    comments = image.comment_set.all()
    context = {
        'image': image,
        'komentari': comments,
    }
    return render(request, 'images/detail.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST['title']
        url = request.POST['url']
        image = Image(
            title = title,
            url = url,
        )
        image.save()
        return redirect(reverse('detail', args=[image.id,]))

    context = {}
    return render(request, 'images/create.html', context)

def create_comment(request, id):
    image = get_object_or_404(Image, pk=id)
    if request.method == "POST":
        author = request.POST['author']
        text = request.POST['text']
        comment = Comment(
            author=author,
            text=text,
            image=image
        )
        comment.save()
    
    return redirect(reverse("detail", args=[image.id,] ))

def like(request, id):
    if request.method == "POST":
        image = get_object_or_404(Image, pk=id)
        image.likes += 1
        image.save()
    return redirect(reverse("detail", args=[image.id,] ))
