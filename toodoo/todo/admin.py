from django.contrib import admin

# Register your models here.
from todo.models import Todo, TodoList

class TodoInLine(admin.TabularInline):
    model = Todo
    extra = 0

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','due_date','completed','favourite',)
    list_filter = ('due_date','completed','favourite')
    search_fields = ('title',)

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (TodoInLine,)
