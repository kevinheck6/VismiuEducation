from django.contrib import admin
from userauths.models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ('email', 'username', 'bio', 'is_staff', 'is_active', 'date_joined')
	list_filter = ('is_staff', 'is_active',)
	search_fields = ('email', 'username',)
	ordering = ('email',)

	filter_horizontal = ()
	fieldsets = ()

admin.site.register(User, UserAdmin)

