"""
URL configuration for filminate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="filminate",
        default_version='1.1.1',
        description="ssafy final-project API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="email"), # 부가정보
        # license=openapi.License(name="mit"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),
    path('user/', include('accounts.urls')),
    
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    
    # path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    # path('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(),
    #         name='password_reset_confirm'),
    
    path('accounts/', include('allauth.urls')),
    path('', include('accounts.urls')),

    # path('dj-rest-auth/google/', include('allauth.socialaccount.urls')),
    # path('api-token-auth/', obtain_auth_token),
    # path('rest-auth/', include('rest_auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
