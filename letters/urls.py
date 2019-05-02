from django.urls import path

from . import views

app_name = "letters" 
urlpatterns = [path('', views.IndexView.as_view(), name='index'),
               path('<int:pk>/', views.LetterDetailView.as_view(), name='letterDetail'),
               path('writeLetter', views.writeLetter, name="writeLetter"),
               path('sendLetter',views.sendLetter,name="sendLetter"),]
