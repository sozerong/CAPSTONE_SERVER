from django.urls import path
from .views import BudgetAPIView

urlpatterns = [
    path("budget/<str:date>/", BudgetAPIView.as_view()),  # GET
    path("budget/", BudgetAPIView.as_view()),             # POST
]
