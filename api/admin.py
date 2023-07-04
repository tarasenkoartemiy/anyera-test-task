from django.contrib import admin
from .models import Pet

admin.site.site_header = "anyera-test-task"
admin.site.index_title = "My super puper admin"


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["id", "nickname", "image", "breed", "owner"]
    ordering = ["nickname"]
    list_per_page = 10
    search_fields = ["nickname__istartswith"]
    list_filter = ["breed", "owner"]