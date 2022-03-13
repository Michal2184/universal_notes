
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import Note, Topic
from .forms import TopicForm, NoteForm
from django.contrib.auth.decorators import login_required

# from django.views.generic import ListView


# Create your views here.
"""
def note_list(request):
    # list of all notes un-filtered 
    notes = Note.published.all()
    return render(request, 'uni_notes/note/list.html', {'notes': notes})
"""
@login_required
def note_detail(request, topic, year, month, day, note):
    """ View single post """
    topics = Topic.objects.filter(author=request.user)
    
    notes = Note.objects.filter(topic__name=topic)
    topic_name = topic
    note = get_object_or_404(Note, slug=note,
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day,
                                   topic__name=topic,
                                   )
    return render(request, 'uni_notes/note/topic_note_detail.html', {'note': note, 'topics': topics, 'notes': notes, 'topic_name': topic_name })

@login_required
def topics_list(request):
    """ list of topics + sidebar"""
    object_list = Topic.objects.filter(author=request.user)
    paginator = Paginator(object_list, 6)  # 6 post per page
    page = request.GET.get('page')
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # if no integer return first page
        topics = paginator.page(1)
    except EmptyPage:
        # if out of range deliver last page
        topics = paginator.page(paginator.num_pages)
     
    return render(request, 'uni_notes/note/topics.html', {'topics': topics, 'page': page, 'object_list': object_list })  # 
'''
# In future can change this to class based view
class TopicListView(ListView):
    queryset = Topic.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'uni_notes/note/topics.html'

    def get(self, request, *args, **kwargs):
'''
@login_required
def topic_content(request, topic):
    """ list of notes belonging to the topic + sidebar """
    object_list = Note.objects.filter(topic__name=topic).filter(author=request.user)
    # checking if topic belongs to owner
    topic_form_edit = Topic.objects.get(name=topic)
    
    #replace variable 'topic' as will use topic objects to produce sidebar
    topic_name = topic
    topics = Topic.objects.filter(author=request.user)
    paginator = Paginator(object_list, 6)  # 6 post per page
    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        # if no integer return first page
        notes = paginator.page(1)
    except EmptyPage:
        # if out of range deliver last page
        notes = paginator.page(paginator.num_pages)
    return render(request, 'uni_notes/note/topic_content.html', {'notes': notes, 'topic_name': topic_name, 'topics': topics, 'page': page, 'object_list': object_list, 'topic_form_edit': topic_form_edit})


@login_required
def new_topic(request):
    """ aadding new topic """
    if request.method != 'POST':
        # create form
        form = TopicForm()
    else:
        # send data via POST
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.author = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('uni_notes:topic_list'))
    context = {'form': form}
    return render(request, 'uni_notes/note/new_topic.html', context)     

@login_required
def new_note(request, topic):
    """ aadding new note for particular topic """
    topic = Topic.objects.get(name=topic)
    if topic.author != request.user:
        raise Http404
    
    if request.method != 'POST':
        # create form
        form = NoteForm()
    else:
        # send data via POST
        form = NoteForm(request.POST)
        if form.is_valid():
            # new_post.slug = slugify(new_post.title)
            new_form = form.save(commit=False)
            new_form.author = request.user
            # form.topic = topic
            new_form.slug = slugify(new_form.title)
            new_form.topic = topic
            new_form.save()
            return HttpResponseRedirect(reverse('uni_notes:topic_content', args=[topic]))
    context = {'topic':topic,'form': form}
    return render(request, 'uni_notes/note/new_note.html', context)            

@login_required
def edit_note(request, note_id):
    """ edit note by its database id number """
    note = Note.objects.get(id=note_id)
    topic = note.topic
    if note.author != request.user:
        raise Http404
    if request.method != 'POST':
        # pre-filling form with existing data
        form = NoteForm(instance=note)
    else:
        # submit edited data
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            # note_detail(request, topic, year, month, day, note)
            # args=[self.topic.name,self.publish.year,self.publish.month,self.publish.day,self.slug]
            return HttpResponseRedirect(reverse('uni_notes:note_detail', args=[note.topic, note.publish.year, note.publish.month, note.publish.day, note.slug]))
    context = {'note': note, 'topic': topic, 'form': form}
    return render(request, 'uni_notes/note/edit_note.html', context)


@login_required
def edit_topic(request, topic_id):
    """ edit note by its database id number """
    topic = Topic.objects.get(id=topic_id)
    
    if topic.author != request.user:
        raise Http404
    if request.method != 'POST':
        # pre-filling form with existing data
        form = TopicForm(instance=topic)
    else:
        # submit edited data
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            # note_detail(request, topic, year, month, day, note)
            # args=[self.topic.name,self.publish.year,self.publish.month,self.publish.day,self.slug]
            return HttpResponseRedirect(reverse('uni_notes:topic_content', args=[topic]))
    context = {'topic': topic, 'form': form}
    return render(request, 'uni_notes/note/edit_topic.html', context)

# delete topic
# Topic.objects.filter(id=1).delete()


# delete note
def delete_note(request, note_id):
    """ delete current note """
    note = Note.objects.get(id=note_id)
    topic_name = note.topic
    topic = Topic.objects.get(name=topic_name)
    Note.objects.filter(id=note_id).delete()
    return HttpResponseRedirect(reverse('uni_notes:topic_content', args=[topic]))

def delete_topic(request, topic_id):
    """ delete current topic and its notes """
    Topic.objects.filter(id=topic_id).delete()
    return HttpResponseRedirect(reverse('uni_notes:topic_list'))

