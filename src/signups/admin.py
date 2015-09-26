from django.contrib import admin

# Register your signup models here.
from signups.models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp
        
admin.site.register(SignUp, SignUpAdmin)

