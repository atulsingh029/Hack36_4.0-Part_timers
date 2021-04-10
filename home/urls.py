from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('signin/', signin),
    path('signup/', signup),
    path('signout/', signout),
    path('story/post/', post_story),
    path('story/delete/', delete_story),
    path('story/edit/', edit_story),
    path('story/<str:story_id>/', read_story),
    path('timeline/', get_timeline),
    path('add/emergency/', add_emergency_contact),
    path('delete/emergency/', delete_emergency_contact),
    path('alert/', alert_trigger),
    path('help/<str:id>', help),
    path('api/voice/', voice)
]

