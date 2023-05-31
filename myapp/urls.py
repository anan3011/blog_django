from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('new',views.newpost_view,name='new'),
    path('add_action',views.add_action,name='add_action'),
    path('delete/<int:pk>/',views.delete_post,name='delete_post')
]