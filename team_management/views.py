from team_management.models import team_member
from team_management.serializers import team_member_serializer
from rest_framework import mixins
from rest_framework import generics

class team_member_view(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    """
    Get/Post handler for team_members
    """
    queryset = team_member.objects.all()
    serializer_class = team_member_serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class team_member_detail_view(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Get/Put/Delete handler for a single object of team_members
    """
    queryset = team_member.objects.all()
    serializer_class = team_member_serializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)