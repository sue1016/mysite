
# Create your views here.
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Letter,Author,Todo
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.utils.safestring import mark_safe
from letters.Morse import Morse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def log(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect(reverse('letters:home'))
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("error")
def login(request):
    return render(request, 'letters/login.html')
def morseEncode(request,input):
    morse = Morse()
    encoded = morse.Encode(input)
    return HttpResponse(encoded)

class IndexView(generic.ListView):
    template_name = 'letters/index.html'
    context_object_name = "letters"
    def get_queryset(self):
        """Return the last five published letters."""
        return Letter.objects.all()

def letterDetail(request,letter_id):
    letter = Letter.objects.get(pk=letter_id)
    context = {
        'letter' : letter,
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
    letter_md = request.POST['letter_md'].replace("\n",r"\n").replace("\r",r"\r")
    title = request.POST['title']
    newLetter = Letter(title = title,
                       letter_md = letter_md,
                       pub_date = timezone.now(),
                       pub_author = author)

    # write the md into a .md file
    mdFileName = "letters/static/letters/md/"+title+".md"
    with open(mdFileName,"w") as f:
	    f.write(letter_md)
    newLetter.save()
    return HttpResponseRedirect(reverse('letters:index'))
#@login_required
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
def todoPlan(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    context = {
        'todo' : todo,
    }    
    return render(request, 'letters/todoPlan.html', context)
def makeToDoPlan(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    #todo.plan_md = request.POST['plan_md']
    todo.plan_md = request.POST['plan_md'].replace("\n",r"\n").replace("\r",r"\r")
    #print(todo.plan_md)
    todo.content = request.POST['content']
    todo.save()
    # write the md into a .md file
    mdFileName = "letters/static/letters/md/todo/"+todo.content+".md"
    with open(mdFileName,"w") as f:
	    f.write(todo.plan_md)
    todo.save()
    return HttpResponseRedirect(reverse('letters:toDoList'))
def makeToDoPlanView(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    context = {
        'todo' : todo,
    }    
    return render(request, 'letters/makeToDoPlanView.html', context)


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
    
  
