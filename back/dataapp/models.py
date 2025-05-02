from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ 유저별 데이터
    date = models.DateField()
    sales = models.IntegerField(default=0)
    expense = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'date')  # ✅ 같은 날짜에는 한 개만 저장 가능
