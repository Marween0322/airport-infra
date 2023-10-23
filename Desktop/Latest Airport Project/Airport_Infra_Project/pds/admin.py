from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import Personal, Payslipstatus, Education, Children, Otherinfo, Other_recognitions, Other_skills, Other_membership, Learning, Vaccine, Bonuses, Payroll

class PersonalAdmin(admin.ModelAdmin):
	"""Admin Funtion"""
	search_fields = ['surname']

admin.site.register(Personal, PersonalAdmin)

admin.site.register(Children)

admin.site.register(Otherinfo)

admin.site.register(Other_membership)

admin.site.register(Other_recognitions)

admin.site.register(Other_skills)


admin.site.register(Learning)
admin.site.register(Payslipstatus)
admin.site.register(Education)
admin.site.register(Bonuses)

admin.site.register(Payroll)

