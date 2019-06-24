from django.urls import path
from . import views
urlpatterns = [

    path('',views.index, name='home'),
    path('add/', views.add_to_cart, name='add'),
    path('xulysoluong/', views.show_cart),
    path('<int:cate_id>/add/', views.add_to_cart1),
    path('product/<int:product_id>/', views.products, name='product'),
    path('product/xulysoluong/',views.show_cart),
    path('cart/<int:product_id>/', views.del_item),
    path('cart/', views.total_cart, name='total_cart'),
    path('cart/order/', views.Order_vip, name='order'),
    path('cart/order/added/', views.Order_Cart, name='order_cart'),
    path('cart/<int:user_id>/order/success/', views.Order_Success, name='success'),
    path('', views.search, name='search'),
    path('capnhat/',views.thaydoisoluong),

     path('listship/', views.ShowListShip),
     path('listship/<int:user_id>/', views.ListShip),

     path('trang403/',views.trang403),

    path('sendmail/',views.send_email),
    path('xatnhan/',views.kiemtracode),

    path('doimatkhau/<slug:code>',views.doimatkhau),








    path('<int:cate_id>/', views.categoris),
    path('<int:cate_id>/xulysoluong/',views.show_cart1),



    path('<int:cate_id>/product/<int:product_id>/', views.product_cates),

    path('<int:cate_id>/product/xulysoluong/',views.show_cart1),

    path('<int:cate_id>/cart/<int:user_id>/', views.my_cart_cate),
    path('<int:cate_id>/product/cart/<int:user_id>/', views.my_cart_cate),
    path('product/cart/<int:user_id>/', views.my_cart_pro, name='my_cart_pro'),
    path('<int:cate_id>/product/cart/<int:user_id>/', views.my_cart_pro_cate),
    path('<int:cate_id>/cart/<int:user_id>/<int:product_id>/', views.del_item_cate),






]