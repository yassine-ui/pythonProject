from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from todo.models import Todo,TodoList
from todo.serializers import TodoSerializer, TodoListSerializer
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['due_date','favourite','completed']
    search_fields = ['title']

class TodolistViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)


