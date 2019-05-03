
# Create your views here.
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Letter,Author,Todo
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .utils import md2html_util
from django.utils.safestring import mark_safe


class IndexView(generic.ListView):
    template_name = 'letters/index.html'
    context_object_name = "letters"
    def get_queryset(self):
        """Return the last five published letters."""
        return Letter.objects.all()

def letterDetail(request,letter_id):
    letter = Letter.objects.get(pk=letter_id)
    md2html = md2html_util.md2html(letter.letter_md)
    context = {
        'letter' : letter,
        'md2html' : mark_safe(md2html),
    }
    return render(request,"letters/letterDetail.html",context)
def home(request):
    return render(request, 'letters/home.html')
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
    letter_md = request.POST['letter_md']
    newLetter = Letter(title = request.POST['title'],
                       letter_md = letter_md,
                       pub_date = timezone.now(),
                       pub_author = author)

    newLetter.save()
    return HttpResponseRedirect(reverse('letters:index'))
def addToDo(request):
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return render(request, 'letters/addToDo.html')
def addToList(request):
    todo_content = request.POST['content']
    todo = Todo(content = todo_content,
                 pub_date = timezone.now(),
                 hasChecked = False,
                 check_date = timezone.now()
               )

    todo.save()
    return HttpResponseRedirect(reverse('letters:toDoList'))
def checkTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.hasChecked = True
    todo.check_date = timezone.now()
    todo.save()
    return HttpResponseRedirect(reverse('letters:toDoList'))
def uncheckToDo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.hasChecked = False
    todo.check_date = timezone.now()
    todo.save()
    return HttpResponseRedirect(reverse('letters:toDoList'))
def deleteToDo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.hasDeleted = True
    todo.save()
    return HttpResponseRedirect(reverse('letters:toDoList'))
class toDoListView(generic.ListView):
    template_name = 'letters/todolist.html'
    context_object_name = "todos"
    def get_queryset(self):
        """Return the last five published letters."""
        return Todo.objects.all().filter(hasChecked=False,hasDeleted=False)
    
class checkedToDosView(generic.ListView):
    template_name = 'letters/checkedToDos.html'
    context_object_name = "todos"
    def get_queryset(self):
        """Return the last five published letters."""
        return Todo.objects.all().filter(hasChecked=True,hasDeleted=False)