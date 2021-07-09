from django.urls import path
from .views import index, faq, about_us

urlpatterns = [
    path('', index, name="homepage"),
    path('faq/', faq, name='fireapp-faq'),
    path('about-us/', about_us, name="about_us"),
]