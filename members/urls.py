from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name = 'main'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>',views.details,name = 'details'),
    path('testing/',views.testing,name = 'testing'),
    path('create/',views.create_member_profile,name = 'create_member_profile'),
    path('success/',views.success_view,name = 'success'),
]