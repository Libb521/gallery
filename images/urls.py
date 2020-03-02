from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url('^today/$',views.today_images,name='imagesToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_images,name='pastImages'), 
    url(r'^search/', views.search_results, name='search_results')
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
