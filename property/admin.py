from django.contrib import admin

from .models import *

class MembershipInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'pure_phone')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ['liked_by']
    inlines = [
        MembershipInline
    ]

@admin.register(Claims)
class ClaimsAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']


