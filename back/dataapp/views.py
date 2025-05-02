from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Budget
from .serializers import BudgetSerializer
from django.shortcuts import get_object_or_404

class BudgetAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, date):
        budget = Budget.objects.filter(user=request.user, date=date).first()
        if budget:
            return Response({
                "sales": budget.sales,
                "expense": budget.expense
            })
        return Response({ "sales": 0, "expense": 0 })

    def post(self, request):
        date = request.data.get("date")
        sales = request.data.get("sales", 0)
        expense = request.data.get("expense", 0)

        budget, created = Budget.objects.get_or_create(
            user=request.user,
            date=date,
            defaults={"sales": sales, "expense": expense}
        )

        if not created:
            budget.sales = sales
            budget.expense = expense
            budget.save()

        return Response({"message": "saved"})
