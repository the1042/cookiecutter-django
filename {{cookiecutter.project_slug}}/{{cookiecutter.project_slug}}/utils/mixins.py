
class SlugMixin:
    readonly_fields = []
    ro_fields = ['slug', ]
    pp_fields = {'slug': ['title', ]}

    def get_readonly_fields(self, request, obj=None):
        if obj:
            if request.user.is_superuser:
                return self.readonly_fields
            else:
                return self.readonly_fields + self.ro_fields
        return self.readonly_fields

    def get_prepopulated_fields(self, request, obj=None):
        if obj:
            return self.prepopulated_fields
        return self.pp_fields
