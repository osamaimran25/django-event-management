from django.urls import path
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from event_management.users.api.views import UserSignup, UserLogin

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register("users", UserViewSet)


app_name = "api"
# urlpatterns = router.urls
urlpatterns = [
    path('users/signup/', UserSignup.as_view(), name='user-signup'),
    path('users/login/', UserLogin.as_view(), name='token_obtain_pair'),

    # Other paths...
]