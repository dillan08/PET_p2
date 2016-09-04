from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.CursosList.as_view()),
    url(r'^(?P<pk>[0-9])/$',views.CursosDetail.as_view()),
]
