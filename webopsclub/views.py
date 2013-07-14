#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
def home(request):
    """
    This is the default landing page view.
    Currently, this page serves the coming_soon.html file
    """ 
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))
