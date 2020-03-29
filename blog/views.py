# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def index(request):
    poster = Post.objects.all()
    return render(request, 'index.html', {'poster': poster})


def post(request, slug):
    """

    :type slug: object
    """
    print(slug)
    return HttpResponse(slug)
