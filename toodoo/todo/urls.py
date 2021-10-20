from rest_framework import routers
from todo.views import TodoViewSet,TodolistViewSet

router = routers.DefaultRouter()
router.register('todos',TodoViewSet)
router.register('todos-Lists',TodolistViewSet)
