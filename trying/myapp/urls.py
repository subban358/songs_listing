from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',views.home, name='home'),
	path('add.html', views.add, name = 'add'),
	path('art.html', views.art, name = 'art'),
	path('login', views.login, name = 'login'),
	path('signup', views.signup, name = 'signup'),
	path('logout', views.logout, name = 'logout'),
	path('rating', views.rating, name = 'rating')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
