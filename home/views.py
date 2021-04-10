from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home '
    }
    return render(request, template_name='index.html', context=context)


def signup(request):
    pass


def signin(request):
    pass


def signout(request):
    pass


def get_timeline(request):
    pass


def post_story(request):
    pass


def delete_story(request):
    pass


def edit_story(request):
    pass


def read_story(request, story_id):
    pass


def add_emergency_contact(request):
    pass


def delete_emergency_contact(request):
    pass


def alert_trigger(request):
    pass


# Rest Framework APIs

def voice(request):
    pass