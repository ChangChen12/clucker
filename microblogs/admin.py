"""Configuration of the admin interface for microblogs."""
from django.contrib import admin
from .models import User
from .models import Post
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users."""
    list_display = [
    'username', 'first_name', 'last_name', 'email', 'is_active',  
    ]

@admin.register(Post)
class UserAdmin2(admin.ModelAdmin):
    list_display2 = [
        'author', 'textline', 'created_at',
    ]
