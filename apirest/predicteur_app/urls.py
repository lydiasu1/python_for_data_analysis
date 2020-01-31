from . import views
from django.urls import path

urlpatterns =[
path('', views.index, name='index'),
path('incidents/<int:incident_id>/', views.incident_detail, name='detail'),
path('incidents/', views.i_want_a_list, name='list_of_incidents'),
path('predict/', views.predict, name='to_predict')
]