from django.contrib import admin

from .models import Category,Post

# configure category
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('cat_id','title','discription','add_date')
    search_fields=('title','cat_id')
    
# configure Post
class PostAdmin(admin.ModelAdmin):
    list_display= ('post_id','title','content','cat')
    search_fields=('title',)
    list_filter=('cat',)

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.site_url = "/blogs"
