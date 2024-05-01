from django.urls import path
from django.conf import settings

from event_management.users.api.views import UserSignup, UserLogin
from event_management.events.api.views import EventManagement



app_name = "api"
urlpatterns = [
    path('users/signup/', UserSignup.as_view(), name='user-signup'),
    path('users/login/', UserLogin.as_view(), name='token_obtain_pair'),
    path('event/', EventManagement.as_view(), name='event-management'),
    path('event/<int:pk>/', EventManagement.as_view(), name='event-management'),
]