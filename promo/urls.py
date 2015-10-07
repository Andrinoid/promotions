
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from slides.views import *

urlpatterns = [
    url(r'^bakendi/', include(admin.site.urls)),

    url(r'^$', frontpage),
    url(r'^login/$', login_user),
    url(r'^logout/$', logout_user),
    url(r'^slides/$', slides),
    url(r'^promotion/(?P<promo_id>\d+)/$', promotion, name='promotion'),
    url(r'^slides/(?P<promo_id>\d+)/$', show_promotion, name='show promotion'),
    url(r'^slidesDemo/$', show_promotion_demo, name='show promotion demo'),
    url(r'^api/addPromotion/$', api_add_promotion),
    url(r'^api/addSlide/$', api_add_slide),
    url(r'^api/updateSlide/$', api_update_slide),
    url(r'^api/updateSlideHtml/$', api_update_slide_html),
    url(r'^api/getSlides/$', api_get_slides),
    url(r'^api/getSlide$', api_get_slide),
    url(r'^api/removeSlide$', api_remove_slide),
    url(r'^api/hideSlide$', api_hide_slide),
    url(r'^api/showSlide$', api_show_slide),
    url(r'^api/updateIndexList$', api_update_indexlist),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
