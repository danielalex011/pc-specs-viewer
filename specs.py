import psutil
import GPUtil
from platform import system, node, release, version, machine, processor

def get_specs():
    try:
        specs = (
            f"System: {system()}\n"
            f"Node Name: {node()}\n"
            f"Release: {release()}\n"
            f"Version: {version()}\n"
            f"Machine: {machine()}\n"
            f"Processor: {processor()}\n"
            f"CPU Usage: {psutil.cpu_percent()}%\n"
            f"Memory Usage: {psutil.virtual_memory().percent}%\n"
            f"Disk Usage: {psutil.disk_usage('/').percent}%\n"
        )

        try:
            gpus = GPUtil.getGPUs()
            for gpu in gpus:
                specs += (
                    f"GPU: {gpu.name}\n"
                    f"GPU Load: {gpu.load * 100}%\n"
                    f"GPU Memory Free: {gpu.memoryFree}MB\n"
                    f"GPU Memory Used: {gpu.memoryUsed}MB\n"
                    f"GPU Temperature: {gpu.temperature}°C\n"
                )
        except Exception as gpu_error:
            specs += f"GPU Error: {gpu_error}\n"

        return specs
    except Exception as e:
        return f"An error occurred: {e}"
