from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^rule/list$', AlertList.as_view(),name="list_rule"),
    #url(r'^subreddit/list$', AlertList.as_view(),name="list_subreddit"),
    
    url(r'^$', 'Bot.views.index.page', name="index"),
    url(r'^login$', 'Bot.views.connection.login.page', name="login_user_bot"),
    url(r'^logout$', 'Bot.views.connection.logout.page', name="logout_user_bot"),
    url(r'^subreddit/create$', 'Bot.views.subreddit.create.page',name="create_subreddit"),
    url(r'^rule/create$', 'Bot.views.rule.create.page',name="create_rule"),
    url(r'^alert/create$', 'Bot.views.alert.create.page',name="create_alert"),
    url(r'^subreddit/list$', 'Bot.views.subreddit.list.page',name="list_subreddit"),
    url(r'^rule/list$', 'Bot.views.rule.list.page',name="list_rule"),
    url(r'^alert/list$', 'Bot.views.alert.list.page',name="list_alert"),
    url(r'^subreddit/(?P<pk>\d+)/update$', 'Bot.views.subreddit.update.page',name="update_subreddit"),
    url(r'^rule/(?P<pk>\d+)/update$', 'Bot.views.rule.update.page',name="update_rule"),
    url(r'^alert/(?P<pk>\d+)/update$', 'Bot.views.alert.update.page',name="update_alert"),
)