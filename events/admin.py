from django.contrib import admin

from .genericcollection import GenericCollectionTabularInline
from .models import Calendar, Event, CalendarRelation, EventRelation, Rule
from .forms import RuleForm


class CalendarRelationInline(GenericCollectionTabularInline):
    model = CalendarRelation


class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    inlines = [CalendarRelationInline]


class EventRelationInline(GenericCollectionTabularInline):
    model = EventRelation


class EventAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('title', 'start', 'end', 'all_day', 'rule')
    list_filter = ('start', 'end', 'all_day', 'rule')
    inlines = [EventRelationInline]


class RuleAdmin(admin.ModelAdmin):
    form = RuleForm


admin.site.register(Rule, RuleAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Calendar, CalendarAdminOptions)
