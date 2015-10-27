from django.conf.urls import include, url
# from django.contrib import admin
# import opencart

urlpatterns = [
    url(r'^', include('opencart.urls', namespace='opencart')),
    # url(r'^admin/', include(admin.site.urls)),
]
