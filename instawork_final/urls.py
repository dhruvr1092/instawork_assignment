"""instawork_final URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path,include

from django.conf.urls import url

from team_management.views import team_member_view, team_member_detail_view

from rest_framework import permissions

from drf_yasg.views import get_schema_view

from drf_yasg import openapi

from team_management.models import roles

# add admin & regular roles if not already added in db
try:
    for i in ["admin", "regular"]:
        if roles.objects.filter(name=i).count() == 0:
            roles.objects.create(name=i)
except:
    pass

#generate Schema view for swagger docs 
schema_view = get_schema_view(
   openapi.Info(
      title="Team members  API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
    url(r'team-members/(?P<pk>\w+)/?$', team_member_detail_view.as_view()),

    url(r'team-members/?$', team_member_view.as_view()),

    url(r'^_docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),

]