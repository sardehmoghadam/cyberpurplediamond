from django.contrib import admin
from .models import contactmodel, blog, technique, maxview, refer, mitigation, subtechnique, tool, TACTIC, actor, malware, emulation
# Register your models here.
admin.site.register(contactmodel)
admin.site.register(blog)
admin.site.register(tool)
admin.site.register(actor)
admin.site.register(malware)
admin.site.register(TACTIC)
admin.site.register(technique)
admin.site.register(subtechnique)
admin.site.register(mitigation)
admin.site.register(maxview)
admin.site.register(refer)
admin.site.register(emulation)
# Register your models here.
