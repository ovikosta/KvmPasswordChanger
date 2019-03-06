from django.db import models


class KvmInfo(models.Model):
    """Kvm model:
    name this kvm name;
    state this online/true or offline/false;
    status kvm is free/true ot busy/false;
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    state = models.BooleanField()
    status = models.BooleanField()
    password = models.CharField(max_length=8, null=True)
    end_access = models.BigIntegerField(null=True)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.name, self.state, self.status, self.password)
