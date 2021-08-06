from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alldata', views.Empviewset)

urlpatterns = [
    path('', views.home, name='home'),
    path('dash', views.dash, name='dash'),
    path('register/', views.register, name='register'),
    path('family2/<int:id>', csrf_exempt(views.family2), name='family2'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/<int:id>', views.update, name='update'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('api/', include(router.urls)),


]