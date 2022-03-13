from cProfile import label
#from dataclasses import fields
#from email import message
from django import forms
from .models import Topic, Note

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'body',]
        labels = {'name':'Title', 'body':'Description'}
        # 428   

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']
        labels = {'title':'Title', 'body':'Notes'}
        
