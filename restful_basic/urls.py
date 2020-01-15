from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails,GenericAPIView

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>', article_detail),
    path('apiview/', ArticleAPIView.as_view()),
    path('apiview/<int:id>', ArticleDetails.as_view()),
    path('genric/apiview/', GenericAPIView.as_view()),
    path('genric/apiview/<int:id>', GenericAPIView.as_view())

]