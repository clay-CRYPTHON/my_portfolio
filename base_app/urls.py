from django.urls import path
from .views import contactPageView, homePageView, experiencePageView

urlpatterns = [
    # path('', homePageView , name='home_page'),
    path('', contactPageView, name='contact_page'),
    # path('', experiencePageView, name='experience_page')
]