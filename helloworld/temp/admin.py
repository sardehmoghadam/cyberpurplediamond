from django.contrib import admin
from .models import contactmodel, blog, technique, maxview, refer, mitigation, subtechnique, TACTIC, actor, malware, emulation, useratt, customadversary, actionsofadversary
from .models import lastestport, exam, userans
# Register your models here.
admin.site.register(contactmodel)
admin.site.register(blog)
admin.site.register(useratt)
admin.site.register(actor)
admin.site.register(malware)
admin.site.register(TACTIC)
admin.site.register(technique)
admin.site.register(subtechnique)
admin.site.register(mitigation)
admin.site.register(maxview)
admin.site.register(refer)
admin.site.register(emulation)
admin.site.register(customadversary)
admin.site.register(actionsofadversary)
admin.site.register(lastestport)
admin.site.register(exam)
admin.site.register(userans)

# Register your models here.
