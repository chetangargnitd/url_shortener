from django.contrib import admin

from .models import URLs

class URLsAdmin(admin.ModelAdmin):
	readonly_fields = ('created',)
	list_display = ['original_url', 'shrinked_url', 'created']


admin.site.register(URLs, URLsAdmin)