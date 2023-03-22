from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [


    path('cbootstrap', views.customer_Bootstrap, name='Bootstrap'),
    path('cbootstrapgrid', views.customer_Bootstrapgrid, name='bootstrapgrid'),
    path('cjavascripttest', views.customer_Javascripttest, name='javascripttest'),
    path('cvariable', views.customer_variable, name='variable'),
    path('cdomsample', views.customer_domsample, name='domsample'),
    path('cToDo', views.customer_ToDo, name='ToDo'),
    path('javascriptsample',views.javascript_sample),
    path('cProductDetail', views.customer_ProductDetail, name='Productdetail'),
    path('cjquerysample', views.customer_jquerysample, name='jquerysample'),
    path('cjquerysample2', views.customer_jquerysample2, name='jquerysample2'),
    path('cjquerysample2', views.customer_jquerysample2, name='jquerysample2'),
    path('cformname', views.customer_formname, name='formname'),
    path('clistsample', views.customer_listsample, name='listsample'),
    path('carraysample', views.customer_arraysample, name='arraysample'),
    path('cinnerwidthsample', views.customer_innerwidthsample,name='innerwidthsample'),
    path('cjqueryvalidation', views.customer_jqueryvalidation,name='jqueryvalidation'),
    path('cminitodolist', views.customer_minitodolist, name='minitodolist'),
    path('ccssgrid',views.customer_cssgrid,name='cssgrid'),
    path('css_broto_sample',views.css_broto_sample,name='css_broto_sample'),


]
