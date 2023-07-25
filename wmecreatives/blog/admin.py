from django.contrib import admin
from . models import Categories, Articles, Images, AnalyticsCode, Photos_collections, Messages

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display  = ["title", "num_views"]

admin.site.register(Articles, ArticleAdmin)


admin.site.register(Categories)
# admin.site.register(Articles)
admin.site.register(Images)
admin.site.register(AnalyticsCode)
admin.site.register(Messages)
