from django.urls import path
from . import views

urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('logout/',views.logout,name='logout'),
    path('viewcustomers/',views.viewcustomers,name='viewcustomers'),
    path('viewenquiries/',views.viewenquiries,name='viewenquiries'),
    path('delenq/<id>',views.delenq,name='delenq'),
    path('viewfeedbacks/',views.viewfeedbacks,name='viewfeedbacks'),
    path('delfeedback/<id>',views.delfeedback,name='delfeedback'),
    path('viewcomplains/',views.viewcomplains,name='viewcomplains'),
    path('delcomplaint/<id>',views.delcomplaint,name='delcomplaint'),
    path('adminchangepswd/',views.adminchangepswd,name='adminchangepswd'),
    path('product/',views.product,name='product'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('delproduct/<id>',views.delproduct,name='delproduct'),
    path('viewcustorders/',views.viewcustorders,name='viewcustorders'),
    
]