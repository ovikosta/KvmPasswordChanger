import string
import random
import time
import base64
import paramiko

from django.conf import settings
from .models import KvmInfo as KI



def password_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def change_password(kvm_name, password):
    #key = paramiko.RSAKey(data=base64.b64decode(b''))
    client = paramiko.SSHClient()
    #client.get_host_keys().add('address', 'ssh-rsa', key)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #add handler exception
    try:
        client.connect(settings.SSH_AUTH_SERVER['address'], username=settings.SSH_AUTH_SERVER['username'], password=settings.SSH_AUTH_SERVER['password'], timeout=2)
    except Exception:
        return {'status': 1}
    _, _, stderr = client.exec_command('net user %s %s' % (kvm_name, password), timeout=5)
    status_code = stderr.channel.recv_exit_status()
    return {'status': status_code}

def check_status(kvm_all):
    now = int(time.time())
    for kvm in kvm_all:
        kvm_obj = KI.objects.get(name=kvm['name'])
        end_access = kvm_obj.end_access / 1000
        if now >= end_access:
            kvm_obj.status = True
        else:
            kvm_obj.status = False
        kvm_obj.save()