"""
URL configuration for post project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지 경로 유지
    path('api/posts/', views.posts, name='posts'),  # api/posts/
    path('api/posts/<slug:slug>/', views.posts_detail, name='post-detail'),  # api/posts/<slug>/
    path('api/search/', views.search_posts, name='search_posts'),  # api/search/
    path('', views.posts, name='home'),  # 루트 경로를 게시글 목록으로 지정
    # path('', admin.site.urls, name='home'),  # 루트 경로를 게시글 목록으로 지정
]

# add at the last
if settings.DEBUG:  # 개발 환경에서만 static 파일을 서빙하도록 설정
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)