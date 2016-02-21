from books.forms import BookForm,UserForm
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth  import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required
def add_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST or None)
		
		if form.is_valid():
			save_it = form.save(commit=False)
			save_it.save()
	return render_to_response("books/add_book.html",locals(),context_instance=RequestContext(request))

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid(): #and profile_form.is_valid():
            	user = user_form.save()
            	user.set_password(user.password)
            	user.save()
            	registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render_to_response(
            'books/register.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
	context = RequestContext(request)

	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password= password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/bookshelf/')
			else:
				return HttpResponse("Your account is disabled")

		else:
			print "Invalid login details: {0},{1}".format(username,password)
			return HttpResponse("Invalid login details supplied.")

	else:
		return render_to_response('books/login.html',{},context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/bookshelf/login/')