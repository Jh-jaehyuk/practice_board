from django.urls import path, include
from rest_framework.routers import DefaultRouter
from board.controller.views import BoardView
router = DefaultRouter()
router.register(r'board', BoardView)  # db랑 엮어주는 역할

urlpatterns = [
    path('', include(router.urls)),
    path('list/', BoardView.as_view({'get': 'list'}), name='board-list'),
]