from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Поля для отображения в списке пользователей
    list_display = ('id', 'username', 'email', 'phone_number', 'average_rating', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'average_rating')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('-average_rating',)  # Сортировка по рейтингу (сначала высокие)

    # Поля для редактирования пользователя
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('phone_number', 'average_rating')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Поля для добавления нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
