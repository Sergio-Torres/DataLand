from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),  
    path('works/', views.workZone, name = 'work_zone'), 
    path('logout/', views.logoutUser, name = 'logout'),

]
#accounts
urlpatterns += [
    
]
#graphics
urlpatterns += [
    path('graph1/', views.graph1View, name='graph1View'),
    path('graph2/', views.graph2View, name='graph2View'),
    path('graph3/', views.graph3View, name='graph3View'),
    path('graph4/', views.graph4View, name='graph4View'),
]

