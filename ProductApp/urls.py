from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.loginUser,name='loginurl'),
    path('logout/',views.logoutUser,name="logouturl"),
    path('signup/',views.signupUser,name='signupurl'),
    path('insert/',views.insertProduct,name = 'inserturl'),
    path('home/<int:pageno>',views.selectProduct,name='homeurl'),
    path('detail/<int:pid>',views.detailFuntion,name='detailurl'),
    path('session/',views.sessionFunction,name='sessionurl')
]