from django.shortcuts import render, HttpResponse, redirect
from models import Event, UserProfile
from forms import EventForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def homepage(request):
    return render(request, 'core/homepage.html')
    
def homepage1(request):
    return render(request, 'core/homepage1.html')
    
def homepage2(request):
    return render(request, 'core/homepage2.html')
    
def index(request):
    event_list = Event.objects.all()
    user_list = User.objects.all()
    data = {'event_list': event_list, 'user_list': user_list }
    
    if request.user.is_authenticated() == True:
        # HOW TO GENERATE THIS PERSONAL FEED
        personal_feed = [
            {'event_name': 'betabeers', 'followings_going': ['pachi','paco']},
            {'event_name': 'wpbilbao', 'followings_going': ['loco','blipy']},
        ]
        data['personal_feed'] = personal_feed
        
    return render(request, 'core/index.html', data) # TO_HTML: event_list, user_list, personal_feed
    
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            f = form.cleaned_data
            event = Event(name=f['name'])
            event.save()
            return HttpResponse("Creado")
    else:
        event_form = EventForm()
        return render(request, 'core/create-event.html', {'event_form': event_form })
        
        
def event(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'core/event.html', {'event': event })
    
def profile(request, user_name):
    owner = False
    user_info = User.objects.get(username=user_name)
    user_profile = UserProfile.objects.get(user=user_info)
    events = user_profile.will_attend_to.all()
    people_following = user_profile.follow_to.all()
    print events
    if request.user.is_authenticated and request.user.username == user_name:
        owner = True
    return render(request, 'core/profile.html', {'user_info': user_info, 'owner': owner, 'events': events, 'people_following': people_following })
    
def join_event(request, event_id):
    if request.user.is_authenticated:
        event = Event.objects.get(id=event_id)
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.will_attend_to.add(event)
        return render(request, 'core/event.html', {'event': event })
        
        
def follow_user(request, user_name):
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user=request.user)
        user_to_follow = User.objects.get(username=user_name)
        user_profile.follow_to.add(user_to_follow)
        return redirect('profile', user_name=user_name)