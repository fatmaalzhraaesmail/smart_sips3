from django.contrib import admin

from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static 
from django.conf import settings
from products.views import addOrderItems, getMyOrders, getOrderById, getOrders, updateOrderToDelivered, updateOrderToPaid

from profiles.views import ProfileView
from products.views import ProductView,CategoryView,OrderView,WishlistView


from rest_framework import routers 

route = routers.DefaultRouter()
route.register("profile", ProfileView, basename="profileview")
route.register("admin/category", CategoryView, basename="categoryview")
route.register("admin/product", ProductView, basename="productview")
# route.register("wishlist", WishlistView, basename="wishlistview")
# route.register("orders/", OrderView,basename="orderview")





urlpatterns = [
    path('/admin/', admin.site.urls),
    path('/api/', include(route.urls)),
    path('/api-auth/', include('rest_framework.urls')),
    # path('accounts/', include('accounts.urls')),
    path('/auth/', include('djoser.urls')),
    path('/auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.social.urls')),
    path('/profile/', include('profiles.urls')),
    path('/getOrders/',getOrders,name="allorders"),
    path('/addOrder/',addOrderItems,name="orders-add"),
    path('/myorders/',getMyOrders,name="myorders"),
    path('/getOrders/<str:pk>/deliver/',updateOrderToDelivered,name="delivered"),
    path('/getOrders/<str:pk>/',getOrderById,name="user-order"),
    path('/getOrders/<str:pk>/pay/',updateOrderToPaid,name="pay"),
    # path('product/', include('products.urls')),
    # path('category/', include('products.urls')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^/.*', TemplateView.as_view(template_name='index.html'))]
