from django.contrib import admin

# Register your models here.

from posts.models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','tittle','photo','recolector_avaliable','classification')
    list_display_links = ('pk','tittle')
    list_editable = ('recolector_avaliable','classification')
    search_fields = (
        'tittle',
        'classification'
    )
    list_filter = (
        'tittle',
        'classification',
        'recolector_avaliable'
    )
    fieldsets = (
        ('Post', {
            'fields' : (
                ('tittle','photo'),
                'definition',
                'sub_tittle',
                'sub_definition'
               
            ),
        }),
        ('Extra_info',{
            'fields' : (
                'recolector_avaliable',
                'color',
                'classification',
                'user',
                'profile'
            )
        }),
        ('metadata',{
            'fields' : (
                'created',
                'modified'
            )
        })
    )
    readonly_fields = ('created','modified')
