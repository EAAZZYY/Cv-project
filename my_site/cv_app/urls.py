from django.urls import path
from . import views
app_name = 'cv_app'

urlpatterns = [
    path('',views.homeview, name='home'),
    path('cvform/', views.cv_form, name = 'cv_form'),
    path('detail/<int:id>/', views.detailview, name='detail'),
    # path('download/<int:id>/', views.download, name='download')
]