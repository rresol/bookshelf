from books.forms import BookForm
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse

def add_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST or None)
		
		if form.is_valid():
			save_it = form.save(commit=False)
			save_it.save()
	return render_to_response("books/add_book.html",locals(),context_instance=RequestContext(request))