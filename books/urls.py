from django.conf.urls import url,patterns

from books import views

urlpatterns = patterns('',
		 url(r'^$', views.add_book, name='add_book'),
	)
