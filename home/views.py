import random
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from .models import Account, Story, Help


def index(request):
    if request.user.is_authenticated:
        return redirect('/timeline')
    latest = Story.objects.filter(status='accepted').order_by('datetime').reverse()
    paged = Paginator(latest, 10)
    page = request.GET.get('page', 1)
    try:
        latest = paged.get_page(page)
    except PageNotAnInteger:
        latest = paged.get_page(1)
    except EmptyPage:
        latest = paged.get_page(paged.num_pages)
    context = {
        'title': 'Home ', 'stories':latest
    }
    return render(request, template_name='index.html', context=context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('/timeline')
    else:
        if request.method == 'POST':
            data = request.POST
            email = data.get('email')
            password1 = data.get('password1')
            password2 = data.get('password2')
            user_type = data.get('you_are')
            profession = data.get('profession')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            image = request.FILES.get('profile_pic')

            duplicate_check = Account.objects.filter(email=email)
            if len(duplicate_check) == 0 and password1 == password2:
                account = Account(username=email, email=email, first_name=first_name, last_name=last_name,
                                  badge_title=profession, badge=user_type, profile_pic=image)
                account.set_password(password2)
                account.save()
                login(request, account)
                return redirect('/timeline')
            else:
                return redirect('/signup?response=Try_Again&prompt=Something_Went_Wrong')
        form = SignUpForm()
        context = {"form": form, "btn_name": "Sign Up", "formname": "Sign Up", "text": "The SafeHouse"
                   }
        return render(request, template_name='form.html', context=context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('/timeline')
    else:
        if request.method == 'POST':
            data = request.POST
            username = data.get('email')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect('/timeline')
            else:
                return redirect('/signin?response=No_Such_User&prompt=Correct_Username_Or_Password_And_Try_Again')
        form = SignInForm()
        context = {"form": form, "btn_name": "Sign In", "formname": "Sign In", "text": "The SafeHouse"
                   }
        return render(request, template_name='form.html', context=context)


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    return redirect('/')


def get_timeline(request):
    if request.user.is_authenticated:
        obj = Account.objects.get(username=request.user)
        helps = Help.objects.filter(receiver=obj)
        if obj.profile_pic =='':
            img = 'add static default url'
        else:
            img =obj.profile_pic.url
        latest = Story.objects.filter(status='accepted').order_by('datetime').reverse()
        paged = Paginator(latest, 10)
        page = request.GET.get('page', 1)
        try:
            latest = paged.get_page(page)
        except PageNotAnInteger:
            latest = paged.get_page(1)
        except EmptyPage:
            latest = paged.get_page(paged.num_pages)

        context = {'profile_pic': img, 'stories': latest, 'badge':obj.badge_title,
                   'helps':helps}
        return render(request, template_name='dashboard.html', context=context)
    else:
        return redirect('/')


def post_story(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES
        title = data.get('title')
        story = data.get('story')
        image = image.get('image')
        if str(image).endswith('.jpg') or str(image).endswith('.png') or str(image).endswith('.jpeg'):
            pass
        else:
            image =''
        if data.get('post_anonymously'):
            writer = None
        elif not request.user.is_authenticated:
            writer = None
        else:
            writer = request.user
        st = Story(title=title, story=story, image=image, writer=writer, storyid=story[0:5]+str(random.randrange(1000000, 9999999)))
        st.save()
        return redirect('/?response=Story_Posted')

    context = {
        'title': 'Post Your Story',
        }
    return render(request, template_name='story_form.html', context=context)



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


def help(request, id):
    if request.method == "POST":
        story = Story.objects.get(storyid=id)
        writer = Account.objects.get(username=story.writer.username)
        helper = Account.objects.get(username=request.user)
        data = request.POST
        contact = data.get('contact_details')
        message = data.get('help_message')
        help = Help(story=story, helper=helper, receiver=writer, contact_details=contact, message=message)
        help.save()
        return redirect('/timeline/?response=YourProposalWasSentToTheStoryWriter')
    form = HelpForm()
    context = {
        'form':form,
        'formname':"Provide Your Help Proposal",
        'btn_name':"Submit"
    }
    return render(request, template_name='form.html', context=context)




# Rest Framework APIs

def voice(request):
    pass