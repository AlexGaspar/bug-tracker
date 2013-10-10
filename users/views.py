# Django import
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# Models import 
from users.models import User

def home(request):
  """Render & display the login page

  :param request: request Object
  :returns: rendered template
  """
  if request.session.get('user') is not None:
    return HttpResponseRedirect( reverse('bugs.views.viewBug') )
  else:
    template_value = {}
    template_value.update(csrf(request))
    return render_to_response('index.html', template_value)

def login(request):
  """ If it's a POST request try to login the user

  :param request: request Object
  :returns: rendered template
  """
  # Deny if it's not a POST request
  if request.method != "POST":
    return HttpResponseRedirect( reverse('users.views.home') )

  # Try to login the user
  try:
    username = request.POST.get('username')
    password = request.POST.get('password')

    # If login/password are invalid it will raise ResourceRequestNotFound
    u = User.login(username, password)
    user = { "username": u.username, "id": u.objectId }
    request.session['user'] = user

    # The user is now logged in, we can redirect him to the dashboard
    return HttpResponseRedirect( reverse('bugs.views.viewBug') )
  except Exception:
    # Assign value to the template
    template_value = {
      'error': 1,
      'page_title': "Login"
    }
    template_value.update(csrf(request))

    return render_to_response('index.html', template_value)

def logout(request):
  """ logout the user

  :param request: request Object
  :returns: HttpResponseRedirect to home
  """
  if request.session.get('user') is not None:
    del request.session['user']

  return HttpResponseRedirect( reverse('users.views.home') )