import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

from .models import KvmInfo as KI
from .forms import ChoiceKvm
from .service import password_generator, change_password, check_status


@login_required
def change_page(request):
    """Render change password KVM page."""
    assert isinstance(request, HttpRequest)
    ch_kvm = ChoiceKvm()
    kvm_all = KI.objects.values('name')
    context = {
        'ch_kvm': ch_kvm,
        'kvm_m9': ((kvm['name'], tuple(KI.objects.filter(name=kvm['name']).values('state', 'status', 'password', 'end_access').order_by('name')))
                                                                        for kvm in kvm_all if 'm9' in kvm['name']),
        'kvm_vdnh': ((kvm['name'], tuple(KI.objects.filter(name=kvm['name']).values('state', 'status', 'password', 'end_access').order_by('name')))
                                                                        for kvm in kvm_all if 'vdnh' in kvm['name']),
        'kvm_idc3': ((kvm['name'], tuple(KI.objects.filter(name=kvm['name']).values('state', 'status', 'password', 'end_access').order_by('name')))
                                                                        for kvm in kvm_all if 'idc3' in kvm['name']),
    }
    check_status(kvm_all)
    return render(request, 'kvmcp/change_block.html', context)

@login_required
def activate(request):
    """Change password for rdp session."""
    assert isinstance(request, HttpRequest)
    kvm_name = request.GET['kvm_name']
    password = password_generator()
    response_info = change_password(kvm_name, password)
    if response_info['status']:
        return HttpResponse(json.dumps({
            'status': 'error'
        }), content_type="application/json")
    else:
        kvm_obj = KI.objects.get(name=kvm_name)
        kvm_obj.password = password
        kvm_obj.save()
        return HttpResponse(json.dumps({
            'status': 'success',
            'password': password,
            #maybe add time for end_access this response
        }), content_type="application/json")

@login_required
def timestamp(request):
    """Add timestamp for equip."""
    #lease in millisecond
    LEASE_2HOURS = 7200000
    kvm_name = request.POST['kvm_name']
    start_time = request.POST['timestamp']
    end_time = int(start_time) + LEASE_2HOURS
    kvm_obj = KI.objects.get(name=kvm_name)
    kvm_obj.end_access = end_time
    kvm_obj.save()

@login_required
def report(request):
    subject = 'Report from app KvmPasswordChanger.'
    to = ['']
    message = request.POST['message']
    print(message)
    # from mail address located in settings
    email = EmailMessage(subject, body=message, to=to)
    response = email.send()
    print(response)