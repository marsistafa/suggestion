
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuggestionListCreateView, SuggestionViewSet

router = DefaultRouter()
router.register(r'suggestions', SuggestionViewSet, basename='suggestion')

urlpatterns = [
    path('suggestions/', SuggestionListCreateView.as_view(), name='suggestion-list-create'),
    path('', include(router.urls)),
]
