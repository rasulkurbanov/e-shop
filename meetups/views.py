from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from meetups.admin import MeetupAdmin

from .forms import RegistrationForm
from .models import Meetup, Participant
# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html',
                  {
                      'show_meetups': True,
                      'meetups': meetups
                  })


def details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == "GET":
            regisration_form = RegistrationForm()

        if request.method == "POST":
            regisration_form = RegistrationForm(request.POST)
            if regisration_form.is_valid():
                participant_username = regisration_form.cleaned_data['username']
                participant_email = regisration_form.cleaned_data['email']
                try:
                    participant_found = Participant.objects.get(username=participant_username)
                    print(participant_found)
                    selected_meetup.participant.add(participant_found)
                    return redirect('confirmation', meetup_slug=meetup_slug)
                except:
                    participant = Participant.objects.create(username=participant_username, email=participant_email)
                    selected_meetup.participant.add(participant)
                    return redirect('confirmation', meetup_slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup': selected_meetup,
            'meetup_found': True,
            'form': regisration_form
        })
    except Exception as exp:
        return render(request, 'meetups/meetup-details.html', {'meetup': None, 'meetup_found': False})


def confirmation(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {'organizer_email': meetup.organizer_email})
