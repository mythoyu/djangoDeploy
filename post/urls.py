from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('post_app.urls')),  # api/로 post_app의 모든 API 경로 연결
]