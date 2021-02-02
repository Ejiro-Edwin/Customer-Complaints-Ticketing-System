from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, TicketSerializer, CategorySerializer
from .models import Ticket, Category, User
from rest_framework.response import Response

# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class TicketViewSet(viewsets.ViewSet):
    def list(self, request):  #  /api/tickets
        tickets = Ticket.objects.all().order_by('-created')
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def create(self, request):  #  /api/tickets
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  #  /api/tickets/<str:id>
        tickets = Ticket.objects.all()
        ticket = get_object_or_404(tickets, pk=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def retrieveticketId(self, request, pk=None, ticket_id=None):  #  /api/tickets/<str:ticketid>
        ticket = Ticket.objects.filter(ticket_id=ticket_id)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def update(self, request, pk=None):  #  /api/tickets/<str:id>
        tickets = Ticket.objects.all()
        ticket = get_object_or_404(tickets, ticket_id=ticket_id)
        serializer = TicketSerializer(instance=ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  #  /api/tickets/<str:id>
        tickets = Ticket.objects.all()
        ticket = get_object_or_404(tickets, pk=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):  #  /api/tickets
        categories = Category.objects.all()
        serializer = TicketSerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):  #  /api/tickets
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  #  /api/tickets/<str:id>
        categories = Category.objects.all()
        category = get_object_or_404(categories, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def update(self, request, pk=None):  #  /api/tickets/<str:id>
        categories = Category.objects.all()
        category = get_object_or_404(categories, pk=pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  #  /api/tickets/<str:id>
        categories = Category.objects.all()
        category = get_object_or_404(categories, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
