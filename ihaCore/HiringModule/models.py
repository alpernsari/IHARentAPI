from django.db import models
from IHAModule.models import IHA
from django.contrib.auth.models import User
class Hiring(models.Model):

    # kiralama tablosu user ve iha ile ilişkiye sahip
    # bu şekilde bağlayarak iha ve user ın özelliklerine erişebiliyorum
    iha = models.ForeignKey(IHA, on_delete=models.PROTECT ,related_name='iha')
    user = models.ForeignKey(User, on_delete=models.PROTECT ,related_name='user')
    
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    # custom permissionlar ayarladım. bu şekilde user ın adminin metodlarına ve sayfalarına erişmemesini sağladım
    # user veya admin rolü olmayanlar için de işlem yapılması engellenir
    class Meta:
        permissions = [
            ("user_list_hiring", "Can user list hirings"),
            ("user_delete", "Can user delete"),
            ("user_update", "Can user update"),
            ("admin_list_hiring", "Can admin list hirings"),
            ("admin_delete", "Can admin delete"),
            ("admin_update", "Can admin update"),
        ]