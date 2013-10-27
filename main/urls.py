from django.conf.urls import patterns, url
from main.views import TadListView

urlpatterns = patterns('',
    url(r'^$', TadListView.as_view(), name="tad_list"),
)
