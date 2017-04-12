from django.conf.urls import include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'restaurants',RestaurantViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^some/', home, name='index'),
     url(r'^restaurant/$', restaurant_list),
     url(r'^restaurant_details/$', restaurant_detail),
     url(r'^test/$', test),
    # url(r'^some/', RestaurantList.as_view(), name='Restaurant-list'),

]
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'testapi.views.home', name='home'),
#     # url(r'^testapi/', include('testapi.foo.urls')),
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )
