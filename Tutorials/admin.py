from django.contrib import admin
from .models import Tutorial,CoursePage,AccountPage,PaymentPage,FreelanceJobPage,ToolsPage,IncentivePage,AboutUsPage
from tinymce.widgets import TinyMCE
from django.db import models


class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(CoursePage)
admin.site.register(AccountPage)
admin.site.register(PaymentPage)
admin.site.register(FreelanceJobPage)
admin.site.register(ToolsPage)
admin.site.register(IncentivePage)
admin.site.register(AboutUsPage)

# Register your models here.

