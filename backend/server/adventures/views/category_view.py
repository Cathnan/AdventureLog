from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from adventures.models import Category, Adventure
from adventures.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user_id=self.request.user)

    @action(detail=False, methods=['get'])
    def categories(self, request):
        """
        Retrieve a list of distinct categories for adventures associated with the current user.
        """
        categories = self.get_queryset().distinct()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user_id != request.user:
            return Response({"error": "User does not own this category"}, status
            =400)
        
        if instance.name == 'general':
            return Response({"error": "Cannot delete the general category"}, status=400)
        
        # set any adventures with this category to a default category called general before deleting the category, if general does not exist create it for the user
        general_category = Category.objects.filter(user_id=request.user, name='general').first()

        if not general_category:
            general_category = Category.objects.create(user_id=request.user, name='general', icon='🌍', display_name='General')
        
        Adventure.objects.filter(category=instance).update(category=general_category)

        return super().destroy(request, *args, **kwargs)