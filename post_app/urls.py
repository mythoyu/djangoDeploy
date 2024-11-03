from django.urls import path
from . import views

# 명확하게 api/posts와 관련된 경로 정리
urlpatterns = [
    path('posts/', views.posts, name='posts'),                    # api/posts/
    path('posts/<slug:slug>/', views.posts_detail, name='post-detail'),  # api/posts/<slug>/
    path('search/', views.search_posts, name='search_posts'),    # api/search/
]

# 8. 백엔드 REST API 최종 정리
# http://localhost:8000/posts (GET)  
# 모든 Posts 모델 데이터 응답 (글 목록 불러오기)

# http://localhost:8000/posts (POST)  
# 클라이언트에서 전달한 데이터 객체 DB에 저장 (글 저장하기)

# http://localhost:8000/posts/슬러그 (GET)  
# 슬러그에 매칭되는 모델 데이터만 응답 (상세글 불러오기)

# http://localhost:8000/posts/슬러그 (PUT) 
# 슬러그에 매칭되는 모델데이터를 같이 전달된 정보고 수정 (상세글 수정)

# http://localhost:8000/posts/슬러그 (DELETE) 
# 슬러그에 매칭되는 모델데이터만 삭제 (상세글 삭제)

# ​http://localhost:8000/post-seach/?search=검색어 (GET) 
# 검색어가 담긴 쿼리값이 포함된 모든 모델 데이터 응답