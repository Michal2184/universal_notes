from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# 4 imports

# Custom manager
#class PublishedManager(models.Manager):
#    def get_queryset(self):
#        return super(PublishedManager, self).get_queryset()# .filter(status='published')


class Topic(models.Model):
    """ Topic that notes will go into """
    name = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def get_absolute_url(self):
        """method for linking separate notes """
        return reverse('uni_notes:topic_content', args=[self.name])

    class Meta:
        """ order that topics will be display in """
        ordering = ("-created",)
    
    def __str__(self):
        return self.name


class Note(models.Model):
    """ Creating Post model """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posted_notes')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Addning manager
    objects = models.Manager()
    # published = PublishedManager()

    def get_absolute_url(self):
        """ method for linking separate notes """
        return reverse('uni_notes:note_detail', args=[self.topic.name,self.publish.year,self.publish.month,self.publish.day,self.slug])

    class Meta:
        """ order that topics will be display in """
        ordering = ("-created",)

    def __str__(self):
        return self.title

