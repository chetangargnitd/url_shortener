from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import URLs

import urllib
import hashlib


def home(request):
	return render(request, 'shorten/index.html')


def shrink(request):
	url = (request.GET["url"])
	c_url = (request.GET["c_url"])
	print(type(c_url))
	encoded_url = url.encode('utf-8')
	hashObject = hashlib.md5(encoded_url)
	shrinked_url = hashObject.hexdigest()[:8]

	if(c_url == ""):
		try:
			check = URLs.objects.get(shrinked_url = shrinked_url)
		except URLs.DoesNotExist:
			entry = URLs(shrinked_url = shrinked_url, original_url = url)
			entry.save()
		return render(request, 'shorten/index.html', {'shrinked_url' : shrinked_url})
	else:
		try:
			check = URLs.objects.get(shrinked_url = c_url)
		except URLs.DoesNotExist:
			entry = URLs(shrinked_url = c_url, original_url = url)
			entry.save()
		return render(request, 'shorten/index.html', {'shrinked_url' : c_url})

def retrieve(request, id):
	target = get_object_or_404(URLs, shrinked_url = id)
	targetURL = target.original_url
	if(targetURL[:4] != 'http'):
		targetURL = 'http://'+targetURL
	return redirect(targetURL)