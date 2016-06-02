from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf import settings
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'app.views.home_fn', name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^author-app/', include('store.urls', namespace='app', app_name='app')),
	url(r'^home/$', 'app.views.home_fn', name = 'home'),
	url(r'^viewallproduct/$', 'app.views.viewall_fn', name = 'viewallproduct'),
	#url(r'^login-user/$', 'app.views.login_user', name ='login-user'),
	url(r'^login/$', 'app.views.login_user', name = 'login'),
	url(r'^register/$','app.views.reg_user',name='register'),
	
	url(r'^aboutus/$','app.views.aboutus_fn',name='aboutus'),
	url(r'^logout/$',  'app.views.logout_user', name = 'logout'),
	
	url(r'^contact_form/$',  'app.views.contact', name = 'contact_form'),
	#url(r'^contact/$', 'app.views.contact', name='contact'),
    url(r'^thanks/$', 'app.views.thanks', name='thanks'),
	url(r'^password_reset_done/$', 'app.views.passdone_fn', name='password_reset_done'),
	url(r'^password_reset_complete/$', 'app.views.passcomplete_fn', name='password_reset_complete'),
	url(r'^iphone_upload/$',  'app.views.iphone_upload', name = 'iphone_upload'),
	url(r'^product_list/$', 'app.views.productlist_fn', name='product_list'),
	url(r'^user_list/$', 'app.views.userlist_fn', name='user_list'),
	url(r'^order_list/$', 'app.views.orderlist_fn', name='order_list'),
	url(r'^iphone_list/$', 'app.views.iphone_listfn', name='iphone_list'),
	url(r'^macbook_list/$', 'app.views.macbook_listfn', name='mackbook_list'),
	url(r'^ipod_list/$', 'app.views.ipod_listfn', name='ipod_list'),
	url(r'^ipad_list/$', 'app.views.ipad_listfn', name='ipad_list'),
	url(r'^message/$', 'app.views.message_fn', name='message'),
	#url(r'^product_details/(?P<id>[0-9]+)/$', 'app.views.product_detailfn', name='product_details'),
	url(r'^prodetail/(?P<id>\d+)/$','app.views.prodetail', name = 'prodetail'),
	url(r'^payment/(?P<id>\d+)/$', 'app.views.payment', name='payment'),
	url(r'^payment/(?P<id>\d+)/$', 'app.views.payment', name='payment'),
	url(r'^search/$', 'app.views.search_fn', name='search'),
	url(r'^prodetail_fn/$', 'app.views.prodetail_fn', name='prodetail_fn'),
	
	url(r'^privacy_policy/$', 'app.views.privacy_fn', name='privacy_policy'),
	url(r'^term_of_use/$', 'app.views.term_fn', name='term_of_use'),
	
	url(r'^deletecomment/(?P<id>\d+)/$', 'app.views.deletecomment', name='deletecomment'),
	
	 url(r'^comments/$', 'app.views.comments_fn', name='comments'),
	
	url(r'^user_profile/(?P<id>\d+)/',  'app.views.userprofile_fn', name = 'user_profile'),
	url(r'^change_password/(?P<id>\d+)/$', 'app.views.change_password', name='change_password'),
	url(r'^admin_panel/$', 'app.views.adminpanel_fn', name='admin_panel'),
	url(r'^view_orders/(?P<id>\d+)/$', 'app.views.vieworders_fn', name='view_orders'),
	
	url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$','app.views.reset_confirm', name='password_reset_confirm'),
    url(r'^reset/$', 'app.views.reset', name='reset'),
	
	url(r'^delete/(?P<id>\d+)/$','app.views.delete', name = 'delete'),
	url(r'^deleteuser/(?P<id>\d+)/$','app.views.deleteuser', name = 'deleteuser'),
	url(r'^ordercancel/(?P<id>\d+)/$','app.views.ordercancel', name = 'ordercancel'),
	url(r'^statuschange/(?P<id>\d+)/$','app.views.statuschange_fn', name = 'statuschange'),
	url(r'^orderbydelivery/$', 'app.views.orderbydelivery', name='orderbydelivery'),
	url(r'^orderbyuser/(?P<id>\d+)/$', 'app.views.orderbyuser', name='orderbyuser'),
	url(r'^orderbytodaydate/$', 'app.views.orderbytodaydate', name='orderbytodaydate'),
	url(r'^orderbyweekdate/$', 'app.views.orderbyweekdate', name='orderbyweekdate'),
	url(r'^orderbymonthdate/$', 'app.views.orderbymonthdate', name='orderbymonthdate'),
	
	#url(r'^userprofileupdate/(?P<id>\d+)/$', 'app.views.userprofileupdate', name='userprofileupdate'),
	url(r'^userprofileupdate_fn/(?P<id>\d+)/$', 'app.views.userprofileupdate_fn', name='userprofileupdate_fn'),
	
		
)	+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)