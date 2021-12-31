from django.urls import path
from . import views

app_name = 'jobboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post', views.create_post, name = "create_post"),
    path('create_stage', views.create_stage, name = "create_stage"),
    path('<int:stage_id>/edit_stage', views.edit_stage, name = "edit_stage"),
    path('<int:stage_id>/delete_stage', views.delete_stage, name = "delete_stage"),
    path('<int:posting_id>/delete_post', views.delete_post, name = "delete_post"),
    path('<int:posting_id>/detail_view', views.detail_view, name = "detail_view"),
    path('<int:posting_id>/edit_post', views.edit_post, name = "edit_post")
]