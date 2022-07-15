from django.contrib import admin
from django.urls import path
from api.views import view_plan,recharge,recharge_history
urlpatterns = [
    path('api/plan/',view_plan),
    path('api/recharge/',recharge),
    path('api/history/',recharge_history),
    path('admin/', admin.site.urls),
]
