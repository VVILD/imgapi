from tastypie.resources import ModelResource
from myapp.models import Foo
from tastypie import fields, utils
from tastypie.authorization import Authorization


class MultipartResource(object):
    def deserialize(self, request, data, format=None):
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart'):
            data = request.POST.copy()
            data.update(request.FILES)

            return data

        return super(MultipartResource, self).deserialize(request, data, format)

class FooResource(MultipartResource,ModelResource):
    img = fields.FileField(attribute="img", null=True, blank=True)
    class Meta:
        queryset = Foo.objects.all()
        resource_name = 'foo'
        authorization=Authorization()
        always_return_data = True
