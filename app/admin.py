from django.contrib.admin.sites import AdminSite

ORDERING = [
    ('auth', [
        'User',
        'Group'
    ]),

    ('location', [
        'Country',
        'State',
        'City',
        'Place'
    ])
]


class Admin(AdminSite):

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        for app_name, object_list in ORDERING:
            app = app_dict[app_name]
            app['models'].sort(key=lambda x: object_list.index(x['object_name']))
            yield app
