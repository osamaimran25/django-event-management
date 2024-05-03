from django.urls import path
from django.conf import settings

from event_management.users.api.views import UserSignup, UserLogin
from event_management.events.api.views import EventManagement, EventList, AttendEvent



app_name = "api"
urlpatterns = [
    path('users/signup/', UserSignup.as_view(), name='user-signup'),
    path('users/login/', UserLogin.as_view(), name='token_obtain_pair'),
    path('event/', EventManagement.as_view(), name='create-event'),
    path('event/<int:pk>/', EventManagement.as_view(), name='event-management'),
    path('events/', EventList.as_view(), name='list-event-management'),
    path('attend/<int:event_id>/', AttendEvent.as_view(), name='attend-event'),

]