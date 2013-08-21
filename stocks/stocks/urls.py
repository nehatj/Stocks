from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stocks.views.home', name='home'),
    # url(r'^stocks/', include('stocks.foo.urls')),
    url(r'^$','stock.views.home'),
#    url(r'^page/$','stock.views.page'),
#    url(r'^search/$','stock.views.search'),
#not needed    url(r'^stock/(?P<stock_id>\d+)/$','stock.views.detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
