from django.urls import path

from . import views

app_name = "letters" 
urlpatterns = [path('', views.index, name='index'),
               path('<int:letter_id>/', views.letterDetail, name='letterDetail'),
               path('writeLetter', views.writeLetter, name="writeLetter"),
               path('sendLetter',views.sendLetter,name="sendLetter"),]
