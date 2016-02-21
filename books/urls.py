from django.conf.urls import url,patterns

from books import views


urlpatterns = patterns('',
		 url(r'^$', views.add_book, name='add_book'),
		 url(r'^register/$',views.register,name='register'),
		 url(r'^login/$',views.user_login,name='login'),
		 url(r'^logout/$',views.user_logout,name='logout')
	)
	