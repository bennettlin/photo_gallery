from django.conf.urls import *
from photo_gallery.photo_items.models import Item, Photo
from django.views.generic import *

urlpatterns = [
    url(r'^$',
        ListView.as_view(model=Item, context_object_name='item_list', template_name='index.html'),
        name='index'
    ),
    url(r'^items/$', 
        ListView.as_view(model=Item, template_name='items_list.html'),
        name='item_list'
    ),
    url(r'^items/(?P<pk>\d+)/$',
        DetailView.as_view(model=Item, template_name='items_detail.html'),
        name='item_detail'
    ),
    url(r'^photos/(?P<pk>\d+)/$',
        DetailView.as_view(model=Photo, template_name='photos_detail.html'),
        name='photo_detail'
    ),
]
