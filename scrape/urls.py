from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^southwest/", views.southwest, name='southwest'),
    url(r"^central/", views.central, name='central'),
    url(r"^midwestern/", views.midwestern, name='midwestern'),
    url(r"^western/", views.western, name='western'),
    url(r"^southeastern/", views.southeastern, name='southeastern'),
    url(r"^northeastern/", views.northeastern, name='northeastern'),
    url(r"^florida/", views.florida, name='florida'),
]

