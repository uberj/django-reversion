from django.test.client import Client
from django.http import HttpResponse, HttpResponseRedirect
import pdb

def disable_reversion(request):
    from reversion.revisions import revision_context_manager
    revision_context_manager.clear()
    revision_context_manager.disabled = True
    return request

@disable_reversion
def index(request):
    client = Client()
    client.get('/admin/')
    return HttpResponse('foobar')
