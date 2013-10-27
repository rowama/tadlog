from django.views.generic.list import ListView
from django.conf import settings
#from tadlog import settings
from main.models import Tad

class TadListView(ListView):
    model=Tad
    context_object_name='tads'
    
    def get_context_data(self, **kwargs):
        context=dict(
            site=dict(
                title=settings.SITE_TITLE
                )
         )
        context.update(kwargs)
        return super(ListView, self).get_context_data(**context)



