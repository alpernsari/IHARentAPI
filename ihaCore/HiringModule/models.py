from django.db import models
from IHAModule.models import IHA
from django.contrib.auth.models import User
class Hiring(models.Model):
    iha = models.ForeignKey(IHA, on_delete=models.PROTECT ,related_name='iha')
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT ,related_name='user')


    class Meta:
        permissions = [
            ("user_list_hiring", "Can user list hirings"),
            ("user_delete", "Can user delete"),
            ("user_update", "Can user update"),
            ("admin_list_hiring", "Can admin list hirings"),
            ("admin_delete", "Can admin delete"),
            ("admin_update", "Can admin update"),
        ]