import psutil
import platform

def get_specs():
    specs = f"System: {platform.system()}\n"
    specs += f"Node Name: {platform.node()}\n"
    specs += f"Release: {platform.release()}\n"
    specs += f"Version: {platform.version()}\n"
    specs += f"Machine: {platform.machine()}\n"
    specs += f"Processor: {platform.processor()}\n"
    specs += f"CPU Usage: {psutil.cpu_percent()}%\n"
    specs += f"Memory Usage: {psutil.virtual_memory().percent}%\n"
    specs += f"Disk Usage: {psutil.disk_usage('/').percent}%\n"
    return specs