from django.urls import path

from . import views

app_name = "letters" 
urlpatterns = [path('index', views.IndexView.as_view(), name='index'),
               path('', views.home, name='home'),
               path('<int:letter_id>/', views.letterDetail, name='letterDetail'),
               path('writeLetter', views.writeLetter, name="writeLetter"),
               path('sendLetter',views.sendLetter,name="sendLetter"),
               path('toDoList',views.toDoListView.as_view(),name="toDoList"),
               path('check/<int:todo_id>/', views.checkTodo, name='checkTodo'),
               path('addToList',views.addToList,name="addToList"),
               path('addToDo',views.addToDo,name="addToDo"),
               path('checkedToDos',views.checkedToDosView.as_view(),name='checkedToDos'),
               path('uncheck/<int:todo_id>/',views.uncheckToDo,name="uncheckToDo"),
               path('deleteToDo/<int:todo_id>/',views.deleteToDo,name="deleteToDo"),
               path('morseEncode/<input>/',views.morseEncode,name="morseEncode"),
               path('login',views.login,name="login"),
               path('log',views.log,name="log"),
               path('todoPlan/<int:todo_id>/',views.todoPlan,name="todoPlan"),
               path('makeToDoPlanView/<int:todo_id>/',views.makeToDoPlanView,name="makeToDoPlanView"),
               path('makeToDoPlan/<int:todo_id>/',views.makeToDoPlan,name="makeToDoPlan"),]

