from django.urls import path, include

# from django.conf.urls import url
from . import views

app_name = 'uni_notes'

urlpatterns = [
    # note views
    path('', views.topics_list, name='topic_list'),
    path('new_topic/', views.new_topic, name='new_topic'),
    # path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_note, name='new_note'),
    # path('', views.TopicListView.as_view(), name='topic_list'),
    path('<topic>/', views.topic_content, name='topic_content'),
    path('<topic>/new_note/', views.new_note, name='new_note'),
    path('<topic>/<int:year>/<int:month>/<int:day>/<slug:note>/', views.note_detail, name='note_detail'),
    path('edit_note/<note_id>', views.edit_note, name='edit_note'),
    path('delete_note/<note_id>', views.delete_note, name="delete_note"),
    path('edit_topic/<topic_id>', views.edit_topic, name='edit_topic'),
    path('delete_topic/<topic_id>', views.delete_topic, name="delete_topic"),
    #path('contact/', views.contact, name='contact'),
]