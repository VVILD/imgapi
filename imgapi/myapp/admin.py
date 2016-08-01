from django.contrib import admin
from myapp.models import Foo

# Register your models here.


class FooAdmin(admin.ModelAdmin):
	list_display=('body','img')

		
admin.site.register(Foo,FooAdmin)
