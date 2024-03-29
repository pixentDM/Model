"""
URL configuration for config project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index), # 서버 실행 시 나타나는 메인 화면
    path("applicant/", include("applicant.urls")),
    path('grades/', include('grades.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # 부트스트랩 적용을 위해 추가 된 코드

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,

)
