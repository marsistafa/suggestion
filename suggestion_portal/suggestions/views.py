
from rest_framework import generics, status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from .models import Suggestion
from .serializers import SuggestionSerializer

class SuggestionListCreateView(generics.ListCreateAPIView):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer

    renderer_classes = [JSONRenderer] 


class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        suggestion = self.get_object()
        suggestion.upvotes += 1
        suggestion.save()
        serializer = self.get_serializer(suggestion)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        suggestion = self.get_object()
        suggestion.downvotes += 1
        suggestion.save()
        serializer = self.get_serializer(suggestion)
        return Response(serializer.data)