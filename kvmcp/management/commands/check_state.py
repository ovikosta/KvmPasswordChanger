#!/usr/bin/env python
from django.core.management.base import BaseCommand, CommandError
import logging
import tempfile

from pythonping import ping
from kvmcp.models import KvmInfo as KI


class Command(BaseCommand):
    """This command check state host use ping."""
    DN_KVM = 'msm.ru'
    help = 'Check available equipment in net.'
    logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        kvm_all = KI.objects.values('name')
        for kvm in kvm_all:
            tmp = tempfile.TemporaryFile(mode='w+t')
            try:
                ping('{kvm_name}.{domain}'.format(kvm_name=kvm['name'], domain=self.DN_KVM),verbose=True, count=3,timeout=1, out=tmp)
            except OSError:
                Command.logger.error("You don't have the permission to socket. Command check_state.")
                break
            tmp.seek(0)
            host = KI.objects.get(name=kvm['name'])
            if 'Request timed out' in tmp.read():
                host.state = False
            else:
                host.state = True
            host.save()
            tmp.close()


