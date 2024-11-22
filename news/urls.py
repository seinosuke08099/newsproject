from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'news'

# URLパターンを登録する変数
urlpatterns = [
    # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),
    
    # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('news/', views.CreatePhotoView.as_view(), name='post'),
    
    # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),

    path('news<int:category>',
         views.CategoryView.as_view(),
         name = 'news_cat'
         ),

    path('news-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'news_detail'
         ),

    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list'
         ),
     
    path('mypage/',views.MypageView.as_view(), name = 'mypage'),


    path('news/<int:pk>/delete/',
         views.PhotoDeleteView.as_view(),
         name = 'news_delete'
         ),

]
 