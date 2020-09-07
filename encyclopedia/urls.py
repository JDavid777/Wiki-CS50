from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("search/",views.search_entry, name="search_entry"),
    path("new_page/", views.new_page, name="new_page"),
    path("new_entry/",views.new_entry,name="new_entry"),
    path("<str:title>/", views.entry,name="entry"),  
    path("edit/<str:title>/",views.edit_entry,name="edit"), 
    path("save_entry", views.save_entry,name="save_entry"),
    path("random_page",views.random_page,name="random_page"),
]
