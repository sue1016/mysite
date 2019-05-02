
# Create your views here.
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Letter,Author
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
class IndexView(generic.ListView):
    template_name = 'letters/index.html'
    context_object_name = "latest_letter_list"

    def get_queryset(self):
        """Return the last five published letters."""
        return Letter.objects.order_by('-pub_date')[:5]

class LetterDetailView(generic.DetailView):
    model = Letter
    template_name = "letters/letterDetail.html"

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