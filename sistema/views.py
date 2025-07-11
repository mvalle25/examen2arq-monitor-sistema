from django.shortcuts import render
from .utils import get_cpu_usage, get_memory_usage, get_disk_usage, get_system_info

def dashboard(request):
    context = {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "system": get_system_info()
    }
    return render(request, 'sistema/dashboard.html', context)