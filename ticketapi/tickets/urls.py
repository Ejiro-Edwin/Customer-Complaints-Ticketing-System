from django.urls import path

from .views import TicketViewSet,UserViewSet, CategoryViewSet

urlpatterns = [
    path('tickets', TicketViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('tickets/<str:pk>', TicketViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('categories', CategoryViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('categories/<str:pk>', CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user',UserViewSet)
]