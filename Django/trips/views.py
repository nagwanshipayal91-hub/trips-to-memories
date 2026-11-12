from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Trip, Trip_detail
from .forms import TripForm, HighlightsForm


# Create your views here.

def home(request):
    return render(request, 'trips/base.html')

def index(request):
    """The home page for trips"""
    return render(request, 'trips/index.html')

@login_required
def cities(request):
    """ Show all trips """
    all_cities = Trip.objects.filter(owner=request.user).order_by("date_added")
    context = {'all_cities':all_cities}
    return render(request,'trips/city.html',context)
    
@login_required
def city_highlights(request, city_id):
    """ show details about a perticular city."""

    city = Trip.objects.get(id = city_id)
    if city.owner != request.user:
        raise Http404
    highlights = city.trip_detail_set.order_by('-date_added')
    context = {'city':city, 'highlights': highlights}
    
    return render(request, 'trips/highlights.html',context)


@login_required
def new_trip(request):
    """Add a new topic."""

    if request.method == 'POST':
     
        # Post data submiited; process data. 
        form = TripForm(request.POST)
        if form.is_valid():
            new_trip = form.save(commit=False)
            new_trip.owner = request.user
            new_trip.save()
            form.save()
            return HttpResponseRedirect(reverse('trips:cities'))
    else:
        form = TripForm()


    context = {'form': form}
    return render(request, 'trips/new_city.html', context)

@login_required
def new_highlights(request, c_id):

    city_name = Trip.objects.get(id=c_id)

    if request.method == 'POST':
        form = HighlightsForm(request.POST)
        if form.is_valid():
            new_highlights = form.save(commit=False)
            new_highlights.city_name = city_name
            new_highlights.save()
            return HttpResponseRedirect(reverse('trips:city_highlights', args=[c_id]))

    else:
        form = HighlightsForm()

    context = {'city_name': city_name, 'form': form}
    return render(request, 'trips/new_highlights.html', context)

@login_required
def edit_highlights(request, highlight_id):

    highlight = Trip_detail.objects.get(id=highlight_id)
    city_name = highlight.city_name

    if city_name.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = HighlightsForm(request.POST, instance=highlight)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('trips:city_highlights', args=[city_name.id])
            )

    else:
        form = HighlightsForm(instance=highlight)

    context = {
        'highlight': highlight,
        'city_name': city_name,
        'form': form
    }

    return render(request, 'trips/edit_highlight.html', context)