from django.conf.urls import url

from fridasnippits.apps.api import views

urlpatterns = [
    url(r'^create-new/?', views.create_new, name="create_new_project"),
    url(r'^update/(?P<nickname>\w+)/(?P<project_slug>[a-zA-Z0-9\-]+)/', views.update_project, name="update_project")
]
