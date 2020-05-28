from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [

    # base
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='inv/login.html'), name="login"),
    path('redirect/', redirect_view, name='admin'),


    # display
    path('laptops/', display_laptops, name="display_laptops"),
    path('desktops/', display_desktops, name="display_desktops"),
    path('mobiles/', display_mobiles, name="display_mobiles"),

    # add item
    path('add_laptop/', add_laptop, name="add_laptop"),
    path('add_desktop/', add_desktop, name="add_desktop"),
    path('add_mobile/', add_mobile, name="add_mobile"),

    # edit item
    path('laptops/edit_item/<int:pk>', edit_laptop, name="edit_laptop"),
    path('desktops/edit_item/<int:pk>', edit_desktop, name="edit_desktop"),
    path('mobiles/edit_item/<int:pk>', edit_mobile, name="edit_mobile"),

    # delete item
    path('laptops/delete/<int:pk>', delete_laptop, name="delete_laptop"),
    path('desktops/delete/<int:pk>', delete_desktop, name="delete_desktop"),
    path('mobiles/delete/<int:pk>', delete_mobile, name="delete_mobile")

]
