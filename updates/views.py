from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from updates.models import Update
from django.utils import simplejson
import json

def update_manager(request,last_update_received=0):
    """
        This is the view for handling GET requests for Updates for the Android
        App
    """
    # Create your views here.
    updates = Update.objects.filter(pk__gt=last_update_received)
    #dicter_of_updates = Update.objects.all().values()
    dict_of_updates = [dict([("id",a.pk),("title",a.title),("message",a.message),("timestamp",str(a.timestamp))]) for a in updates ] 
    return HttpResponse(json.dumps(dict_of_updates), mimetype='application/json' )
    #return HttpResponse('Hello World!')
