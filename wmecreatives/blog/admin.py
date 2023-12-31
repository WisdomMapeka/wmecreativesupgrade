from django.contrib import admin
from . models import Categories, Articles, Images, AnalyticsCode, Photos_collections, Messages, Comments

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display  = ["title", "num_views"]
admin.site.register(Articles, ArticleAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display  = ["name", "is_series"] 
admin.site.register(Categories, CategoriesAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display  = ["name", "comment", "blog"] 
admin.site.register(Comments, CommentsAdmin)

# admin.site.register(Articles)
admin.site.register(Images)
admin.site.register(AnalyticsCode)
admin.site.register(Messages)
