from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate'),
]
