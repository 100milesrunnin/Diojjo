from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth import views as auth_views

from authentication import views as diojo_auth_views
from account import views as account_views
from article import views as article_views
from search import views as search_views
from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', article_views.articles, name='articles'),
    url(r'^signup/', diojo_auth_views.signup, name='signup'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^login/$', auth_views.login, {
        'template_name': 'authentication/login.html'}, name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^ajax/validate_username/$', diojo_auth_views.validate_username,
        name='validate_username'),

    url(r'^profile/edit/$', account_views.edit, name='edit'),
    url(r'^profile/picture/$', account_views.picture, name='picture'),
    url(r'^profile/upload_picture/$', account_views.upload_picture,
        name='upload_picture'),
    url(r'^user/(?P<username>[^/]+)/$', account_views.profile,
        name='profile'),
    url(r'^user/(?P<username>[^/]+)/liked/$', account_views.liked,
        name='liked'),

    url(r'^post/new/$', article_views.new_article, name='new_article'),
    url(r'^new/$', article_views.new, name='new'),
    url(r'^post/(?P<pk>[0-9]+)/$', article_views.article_detail,
        name='article_detail'),
    url(r'^post/comment/$', article_views.comment, name='comment'),
    url(r'^remove/$', article_views.remove, name='remove'),
    url(r'^delete/$', article_views.delete_article, name='delete'),
    url(r'^edit/(?P<pk>[0-9]+)/$', article_views.edit, name='edit'),
    url(r'^like/', article_views.like, name='like'),

    url(r'^search/$', search_views.search, name='search'),
    url(r'^tag/(?P<tag_name>.+)/$', search_views.tag, name='tag'),

    url(r'^admin/', include(admin.site.urls)),
]
