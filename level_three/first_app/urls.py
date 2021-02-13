from django.urls import path
from first_app import views
urlpatterns = [
    path('',views.form_name_view,name = 'form_name')
]