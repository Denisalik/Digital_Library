from django.conf.urls import url
from users_view import views
from django.urls import path

"""
Defined routes.

/api/user_view/thematic_pages_list: GET
/api/user_view/not_available_pages_list: GET
/api/user_view/thematic_page_uploads/:pk: GET
/api/user_view/request_read_rights/:pk: GET
/api/user_view/bookmark_list: GET
/api/user_view/bookmark/add/:page_title: POST
/api/user_view/bookmark/:bookmark_pk/:upload_pk: POST
/api/user_view/bookmark_uploads/:pk: GET
"""

urlpatterns = [
    url('thematic_pages_list', views.thematic_pages_list),
    url('not_available_pages_list', views.not_available_pages_list),
    url('thematic_page_uploads/(?P<pk>[0-9]+)$', views.thematic_page_uploads),
    url('request_read_rights/(?P<pk>[0-9]+)', views.request_read_rights),
    url('bookmark/(?P<bookmark_pk>[0-9]+)/(?P<upload_pk>[0-9]+)', views.add_to_bookmark),
    path('bookmark/add/<str:page_title>/', views.add_bookmark),
    url('bookmark_list', views.bookmarks_list),
    url('bookmark_uploads/(?P<pk>[0-9]+)', views.bookmark_uploads)
]
