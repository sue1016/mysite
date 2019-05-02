
# Create your views here.
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Letter,Author
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
def index(request):
    latest_letter_list = Letter.objects.order_by('-pub_date')[:5]
    context = {
        'latest_letter_list': latest_letter_list,
    }
    
    return render(request, 'letters/index.html', context)
def letterDetail(request, letter_id):    
    try:
        letter = Letter.objects.get(pk=letter_id)
    except Letter.DoesNotExist:
        raise Http404("Letter does not exist")
    return render(request, 'letters/letterDetail.html', {'letter': letter})

def writeLetter(request):
    authors = Author.objects.all()
    context = {'authors':authors,}
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return render(request, 'letters/writeLetter.html', context)

def sendLetter(request):
    author_id = request.POST['author_id']
    author = Author.objects.get(pk=author_id)
    newLetter = Letter(title = request.POST['title'],
                       letter_md = request.POST['letter_md'],
                       pub_date = timezone.now(),
                       pub_author = author)
    newLetter.save()
    return HttpResponseRedirect(reverse('letters:index'))