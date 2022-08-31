from django.urls import path
from .views import ProfileListView, ProfileDetailView

profiles_patterns = ([
    path('',ProfileListView.as_view(),name='list'),
    path('view/<slug:username>',ProfileDetailView.as_view(),name='view'),
],'profiles')