from django.urls import path
from .views import Index, add_new, valid_data, invalid_data

urlpatterns = [
    path('', Index, name="Index"),
    path('add_new/', add_new, name="Add New"),
    path('successful/', valid_data, name="Valid Data"),
    path('unsuccessful/', invalid_data, name="Invalid Data")
]
