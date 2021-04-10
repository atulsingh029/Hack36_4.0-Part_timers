from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('/timeline')
    context = {
        'title': 'Home '
    }
    return render(request, template_name='index.html', context=context)


def signup(request):
    pass


def signin(request):
    if request.user.is_authenticated:
        return redirect('/timeline')
    else:
        return render(request, template_name='login.html')


def signout(request):
    pass


def get_timeline(request):
    if request.user.is_authenticated:
        context ={}
        return render(request, template_name='dashboard.html', context=context)
    else:
        return redirect('/')


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