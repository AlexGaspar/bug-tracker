from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^bug/create/post', 'bugs.views.createBug'),
    url(r'^bug/create', 'bugs.views.formBug'),
    url(r'^bug/view/single','bugs.views.singleViewBug'),
    url(r'^bug/view', 'bugs.views.viewBug'),
    url(r'^login', 'users.views.login'),
    url(r'^logout', 'users.views.logout'),
    url(r'^', 'users.views.home'),
)
