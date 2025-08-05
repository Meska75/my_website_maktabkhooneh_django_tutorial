"""
URL configuration for tourist_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
import debug_toolbar
from django.contrib.auth import views as auth_views
from accounts.forms import CustomPasswordResetForm




sitemaps = {
    "static": StaticViewSitemap,
    "blog" : BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path(
        "sitemap.xml",sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",),
    path('summernote/', include('django_summernote.urls')),
    path('robots.txt', include('robots.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('captcha/', include('captcha.urls')),
    
    #forgot password paths
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name='accounts\password_change_form.html'
            ),
        name="password_change"
    ),

    path("password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name='accounts\password_reset.html',
            form_class=CustomPasswordResetForm,
            ),
        name="password_reset"
        ),

    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts\password_reset_done.html'
            ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts\password_reset_confirm.html'     
        ),
        name="password_reset_confirm",
    ),
    
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts\password_reset_complete.html'
        ),
        name="password_reset_complete",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
