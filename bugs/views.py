# Django import
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# Models import
from bugs.models import Bug
from users.models import User

def viewBug(request):
  """ Render the view.html template with the list of bugs

  :param request: request Object
  :returns: rendered template
  """
  if request.session.get('user') is None:
    return HttpResponseRedirect( reverse('users.views.home') )

  # Retrieve all Bugs From Parse
  listBugs = Bug.Query.all()

  # Assign value to the template
  template_value = {
    'page_title' : 'View all bugs',
    'listBugs' : listBugs
  }

  return render_to_response('bugs/view.html', template_value)

def singleViewBug(request):
  """ Render the single.html template with a selected bug

  :param request: request Object
  :returns: rendered template
  """

  if request.session.get('user') is None:
    return HttpResponseRedirect( reverse('users.views.home') )

  bugId = request.GET.get('id')
  # Redirect if id is not set
  if bugId is None:
    return HttpResponseRedirect('/')

  bugId = request.GET.get('id')
  bug = Bug.Query.get(objectId=bugId)
  user = User.Query.get(objectId=bug.assignTo)

  # Assign value to the template
  template_value = {
    'page_title': bug.title,
    'bug': bug,
    'assigned_to': user.username
  }

  return render_to_response('bugs/single.html', template_value)

def createBug(request):
  """ If it's a POST request add the bug to Parse

  :param request: request Object
  :returns: HttpResponseRedirect to the list of bugs
  """
  if request.session.get('user') is None:
    return HttpResponseRedirect( reverse('users.views.home') )

  if request.method == "POST":
    title = request.POST.get('title')
    description = request.POST.get('description')
    userId = request.POST.get('to')

    # Persist the data using parse
    newBug = Bug(title=title,description=description, assignTo=userId)
    newBug.save()

  return HttpResponseRedirect( reverse('bugs.views.viewBug') )

def formBug(request):
  """ Render the form.html template

  :param request: request Object
  :returns: HttpResponseRedirect to the list of bugs
  """
  if request.session.get('user') is None:
    return HttpResponseRedirect( reverse('users.views.home') )

  # Retrieve all User from Parse
  listUsers = User.Query.all()

  # Assign value to the template
  template_value = {
    'page_post'  : reverse('bugs.views.createBug'),
    'page_title' : 'Add a new bug',
    'assignUser' :listUsers
  }
  template_value.update(csrf(request))

  return render_to_response('bugs/form.html', template_value)