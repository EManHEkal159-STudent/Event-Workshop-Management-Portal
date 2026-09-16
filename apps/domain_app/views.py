from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Registration

def home(request):
    """View to list all upcoming events."""
    events = Event.objects.all().order_by('-date_time')
    return render(request, 'domain_app/home.html', {'events': events})

def event_detail(request, event_id):
    """View to display details of a specific event."""
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'domain_app/event_detail.html', {'event': event})

@login_required
def register_event(request, event_id):
    """View to handle event registration for logged-in users."""
    event = get_object_or_404(Event, id=event_id)
    
    # Check if user is already registered
    already_registered = Registration.objects.filter(user=request.user, event=event).exists()
    
    if not already_registered:
        Registration.objects.create(user=request.user, event=event)
        messages.success(request, f"Successfully registered for {event.title}!")
    else:
        messages.info(request, "You are already registered for this event.")
        
    return redirect('dashboard')

@login_required
def dashboard(request):
    """View to display user's registered events."""
    registrations = Registration.objects.filter(user=request.user).select_related('event')
    return render(request, 'domain_app/dashboard.html', {'registrations': registrations})