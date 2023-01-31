from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('itemList/', views.itemList),
    path('item/<int:pk>/', views.itemDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
