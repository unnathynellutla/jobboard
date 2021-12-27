from django.urls import path
from . import views

app_name = 'jobboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:posting_id>/', views.edit_post, name='edit_post'),
]