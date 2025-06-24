from django.urls import path
from .views import PortfolioListView, ProjectDetailView

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio_list'),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
] 