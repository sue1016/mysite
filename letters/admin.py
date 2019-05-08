from django.contrib import admin

from .models import Author,Letter,Todo,ChatBot
from solo.admin import SingletonModelAdmin

admin.site.register(ChatBot, SingletonModelAdmin)

# There is only one item in the table, you can get it this way:

# get_solo will create the item if it does not already exist
chatbot = ChatBot.get_solo()
admin.site.register(Author)
admin.site.register(Letter)
admin.site.register(Todo)