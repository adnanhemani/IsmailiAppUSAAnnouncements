from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .models import Link


def southwestern(request):
    link = Link.objects.filter(region_name="southwestern")[0]
    return HttpResponseRedirect(link.region_link)


def central(request):
    link = Link.objects.filter(region_name="central")[0]
    return HttpResponseRedirect(link.region_link)


def midwestern(request):
    link = Link.objects.filter(region_name="midwestern")[0]
    return HttpResponseRedirect(link.region_link)


def western(request):
    link = Link.objects.filter(region_name="western")[0]
    return HttpResponseRedirect(link.region_link)


def southeastern(request):
    link = Link.objects.filter(region_name="southeastern")[0]
    return HttpResponseRedirect(link.region_link)


def northeastern(request):
    link = Link.objects.filter(region_name="northeastern")[0]
    return HttpResponseRedirect(link.region_link)


def florida(request):
    link = Link.objects.filter(region_name="florida")[0]
    return HttpResponseRedirect(link.region_link)

