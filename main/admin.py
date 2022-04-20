from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [("Title/date", {'fields': ['title', 'published']}),
                 ("Content", {"fields": ['content']}),
                 ("URL", {"fields": ['slug']}),
                 ("Series", {"fields": ['series']})]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)

admin.site.register(Tutorial, TutorialAdmin)
