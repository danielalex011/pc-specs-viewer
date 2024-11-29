import psutil
import GPUtil
from platform import system, node, release, version, machine, processor

def get_specs():
    try:
        specs = f"System: {system()}\n"
        specs += f"Node Name: {node()}\n"
        specs += f"Release: {release()}\n"
        specs += f"Version: {version()}\n"
        specs += f"Machine: {machine()}\n"
        specs += f"Processor: {processor()}\n"
        specs += f"CPU Usage: {psutil.cpu_percent()}%\n"
        specs += f"Memory Usage: {psutil.virtual_memory().percent}%\n"
        specs += f"Disk Usage: {psutil.disk_usage('/').percent}%\n"

        # Get GPU information
        gpus = GPUtil.getGPUs()
        if gpus:
            for gpu in gpus:
                specs += f"GPU: {gpu.name}\n"
                specs += f"GPU Load: {gpu.load * 100}%\n"
                specs += f"GPU Memory Free: {gpu.memoryFree}MB\n"
                specs += f"GPU Memory Used: {gpu.memoryUsed}MB\n"
                specs += f"GPU Memory Total: {gpu.memoryTotal}MB\n"
                specs += f"GPU Temperature: {gpu.temperature}°C\n"
        else:
            specs += "GPU: No GPU found\n"

        return specs
    except Exception as e:
        return f"An error occurred while retrieving specs: {e}"