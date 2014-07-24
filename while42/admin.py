from django.contrib import admin
from .models import Chapter
from .models import Member
from .models import Photo


class PhotoInline(admin.StackedInline):
    model = Photo


class MemberAdmin(admin.ModelAdmin):
    list_filter = ['chapter']
    search_fields = ['first_name', 'last_name', 'school', 'work']
    inlines = [PhotoInline]


admin.site.register(Chapter)
admin.site.register(Photo)
admin.site.register(Member, MemberAdmin)
