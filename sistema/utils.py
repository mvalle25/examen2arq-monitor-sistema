import psutil
import platform

def get_cpu_usage():
    try:
        return psutil.cpu_percent(interval=1)
    except Exception as e:
        return f"Error: {e}"

def get_memory_usage():
    try:
        mem = psutil.virtual_memory()
        return {"total": round(mem.total / (1024**3), 2),
                "used": round(mem.used / (1024**3), 2),
                "percent": mem.percent}
    except Exception as e:
        return f"Error: {e}"

def get_disk_usage():
    try:
        disk = psutil.disk_usage('/')
        return {"total": round(disk.total / (1024**3), 2),
                "used": round(disk.used / (1024**3), 2),
                "free": round(disk.free / (1024**3), 2),
                "percent": disk.percent}
    except Exception as e:
        return f"Error: {e}"

def get_system_info():
    try:
        return {
            "os": platform.system(),
            "os_version": platform.release(),
            "cpu_cores": psutil.cpu_count(logical=True)
        }
    except Exception as e:
        return f"Error: {e}"