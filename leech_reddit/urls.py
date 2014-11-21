from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leech_reddit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^reddit_bot/', include('Bot.urls',namespace='Bot')),
    url(r'^admin/', include(admin.site.urls)),
)
