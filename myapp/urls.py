from tkinter.font import names
from django.contrib import admin
from django.urls import path
from .import views
from .views import index
from .views import sign_up, sign_in
from .views import payment, create_checkout_session, success, cancel

urlpatterns = [
    path('', views.index, name='index'),
    path('productDetails/', views.productDetails, name='productDetails'),
    path('product/', views.product, name='product'),
    path('appl/', views.appl, name='appl'),
    path('appl_det/', views.appl_det, name='appl_det'),
    path('beauty/', views.beauty, name='beauty'),
    path('beauty_det/', views.beauty_det, name='beauty_det'),
    path('cam/', views.cam, name='cam'),
    path('cam_details/', views.cam_details, name='cam_details'),
    path('fru/', views.fru, name='fru'),
    path('fru_det/', views.fru_det, name='fru_det'),
    path('fur/', views.fur, name='fur'),
    path('fur_det/', views.fur_det, name='fur_det'),

    path('gro/', views.gro, name='gro'),
    path('gro_det/', views.gro_det, name='gro_det'),
    path('headset/', views.headset, name='headset'),
    path('headset_det/', views.headset_det, name='headset_det'),

    path('jew/', views.jew, name='jew'),
    path('jew_det/', views.jew_det, name='jew_det'),

    path('lap/', views.lap, name='lap'),
    path('lap_det/', views.lap_det, name='lap_det'),

    path('mob_product/', views.mob_product, name='mob_product'),
    path('mob_product_det/', views.mob_product_det, name='mob_product_det'),

    path('shoe/', views.shoe, name='shoe'),
    path('shoe_det/', views.shoe_det, name='shoe_det'),

    path('sta/', views.sta, name='sta'),
    path('sta_det/', views.sta_det, name='sta_det'),

    path('top/', views.top, name='top'),
    path('top_det/', views.top_det, name='top_det'),

    path('tshirt/', views.tshirt, name='tshirt'),
    path('tshirt/', views.tshirt_det, name='tshirt_det'),

    path('veg/', views.veg, name='veg'),
    path('veg_det/', views.veg_det, name='veg_det'),

    path('watch/', views.watch, name='watch'),
    path('watch_det/', views.watch_det, name='watch_det'),

    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('payment/<str:product_name>/<int:product_price>/', views.payment, name='payment'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),

    path('add_to_cart/<str:product_name>/<int:product_price>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),

]