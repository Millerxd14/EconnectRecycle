''' user admin classes'''

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin




# Models
from django.contrib.auth.models import User
from users.models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','phone_number','direction')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','direction')
    search_fields = (
        'user__username',
        'user__email',
        'person_type', 
        'company_name'
    )
    list_filter = (
        'person_type',
        'is_collector',
        'is_productor'
    )
    fieldsets = (
        ('Profile', {
            'fields' : (
                ('user','phone_number'),
                'direction',
                'profile_picture',
            ),
        }),
        ('Extra_info',{
            'fields' : (
                'person_type',
                ('company_name','dni'),
                'is_collector',
                'is_productor',
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


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'


class UserAdmin(BaseUserAdmin):
    ''' add profile admin to base user admin'''
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User,UserAdmin)