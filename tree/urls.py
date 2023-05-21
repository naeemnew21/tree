from django.urls import path
from . import views
from . import api

app_name = 'tree'


urlpatterns = [
    path('', views.index , name = 'index'),
    path('naeem', views.naeem , name = 'naeem'),

    path('branch-create', api.CreateBranch.as_view(), name = 'branch-create'),
    path('branch-update/<int:pk>', api.BranchUpdate.as_view(), name = 'branch-update'),

    path('naeem/branch-create', api.CreateFamilyBranch.as_view(), name = 'family-branch-create'),
    path('naeem/branch-update/<int:pk>', api.FamilyBranchUpdate.as_view(), name = 'family-branch-update'),
]
