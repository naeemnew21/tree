from django.urls import path
from . import views 
from . import api 

app_name = 'tree'


urlpatterns = [
    path('', views.index , name = 'index'),

    path('branch-create', api.CreateBranch.as_view(), name = 'branch-create'),
    path('branch-update/<int:pk>', api.BranchUpdate.as_view(), name = 'branch-update'),
]
