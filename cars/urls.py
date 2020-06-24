from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path
from cars import views


urlpatterns = [
    path('cars/', views.CarList.as_view(), name='car_list'),
    path('cars/<int:pk>/', views.CarDetail.as_view(), name='car_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
