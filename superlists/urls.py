from django.conf.urls import include, url
from django.contrib import admin
from lists import views

urlpatterns = [
	url(r'^', views.home_page, name='home')
    # url(r'^admin/', include(admin.site.urls)),
]
