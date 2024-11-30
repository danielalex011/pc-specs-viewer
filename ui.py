import tkinter as tk
from tkinter import ttk
import psutil
import GPUtil
from specs import get_specs

# Color palette for dark theme
BACKGROUND_COLOR = "#1e1e1e"
CARD_COLOR = "#2e2e2e"
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#9b59b6"

def get_network_info():
    net_io = psutil.net_io_counters()
    network_info = f"Bytes Sent: {net_io.bytes_sent}\n"
    network_info += f"Bytes Received: {net_io.bytes_recv}\n"
    network_info += f"Packets Sent: {net_io.packets_sent}\n"
    network_info += f"Packets Received: {net_io.packets_recv}\n"
    return network_info

def show_network_info():
    network_info = get_network_info()
    for widget in detail_frame.winfo_children():
        widget.destroy()

    network_label = tk.Label(detail_frame, text="Network Information", font=("Helvetica", 14, "bold"), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    network_label.pack(pady=10)

    network_display = tk.Text(detail_frame, width=50, height=10, font=("Consolas", 10), bg=CARD_COLOR, fg=TEXT_COLOR, borderwidth=0)
    network_display.insert(tk.END, network_info)
    network_display.configure(state='disabled')
    network_display.pack(pady=10)

def show_processor_info():
    for widget in detail_frame.winfo_children():
        widget.destroy()

    processor_label = tk.Label(detail_frame, text="Processor Information", font=("Helvetica", 14, "bold"), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    processor_label.pack(pady=10)

    processor_display = tk.Text(detail_frame, width=50, height=10, font=("Consolas", 10), bg=CARD_COLOR, fg=TEXT_COLOR, borderwidth=0)
    processor_display.insert(tk.END, "Processor details go here...")
    processor_display.configure(state='disabled')
    processor_display.pack(pady=10)

def show_memory_info():
    for widget in detail_frame.winfo_children():
        widget.destroy()

    memory_label = tk.Label(detail_frame, text="Memory Information", font=("Helvetica", 14, "bold"), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    memory_label.pack(pady=10)

    memory_display = tk.Text(detail_frame, width=50, height=10, font=("Consolas", 10), bg=CARD_COLOR, fg=TEXT_COLOR, borderwidth=0)
    memory_display.insert(tk.END, "Memory details go here...")
    memory_display.configure(state='disabled')
    memory_display.pack(pady=10)

def show_storage_info():
    for widget in detail_frame.winfo_children():
        widget.destroy()

    storage_label = tk.Label(detail_frame, text="Storage Information", font=("Helvetica", 14, "bold"), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    storage_label.pack(pady=10)

    storage_display = tk.Text(detail_frame, width=50, height=10, font=("Consolas", 10), bg=CARD_COLOR, fg=TEXT_COLOR, borderwidth=0)
    storage_display.insert(tk.END, "Storage details go here...")
    storage_display.configure(state='disabled')
    storage_display.pack(pady=10)

def show_gpu_info():
    gpus = GPUtil.getGPUs()
    for widget in detail_frame.winfo_children():
        widget.destroy()

    gpu_label = tk.Label(detail_frame, text="GPU Information", font=("Helvetica", 14, "bold"), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    gpu_label.pack(pady=10)

    if gpus:
        for gpu in gpus:
            gpu_info = f"GPU: {gpu.name}\n"
            gpu_info += f"GPU Load: {gpu.load * 100}%\n"
            gpu_info += f"GPU Memory Free: {gpu.memoryFree}MB\n"
            gpu_info += f"GPU Memory Used: {gpu.memoryUsed}MB\n"
            gpu_info += f"GPU Memory Total: {gpu.memoryTotal}MB\n"
            gpu_info += f"GPU Temperature: {gpu.temperature}°C\n"
            gpu_display = tk.Text(detail_frame, width=50, height=10, font=("Consolas", 10), bg=CARD_COLOR, fg=TEXT_COLOR, borderwidth=0)
            gpu_display.insert(tk.END, gpu_info)
            gpu_display.configure(state='disabled')
            gpu_display.pack(pady=10)
    else:
        no_gpu_label = tk.Label(detail_frame, text="No GPU found", font=("Helvetica", 14, "bold"), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        no_gpu_label.pack(pady=10)

def create_ui(specs_text):
    def refresh_specs():
        try:
            new_specs = get_specs()
            overview_display.configure(state='normal')
            overview_display.delete(1.0, tk.END)
            overview_display.insert(tk.END, new_specs)
            overview_display.configure(state='disabled')
        except Exception as e:
            overview_display.configure(state='normal')
            overview_display.delete(1.0, tk.END)
            overview_display.insert(tk.END, f"An error occurred while refreshing specs: {e}")
            overview_display.configure(state='disabled')

    global root, detail_frame, overview_display
    root = tk.Tk()
    root.title("PC Specs")
    root.geometry("1000x600")
    root.configure(bg=BACKGROUND_COLOR)

    # Add a title label
    title_label = tk.Label(root, text="Your PC Specifications", font=("Helvetica", 18, "bold"), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    title_label.pack(pady=20)

    # Add a frame for the main dashboard
    dashboard_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
    dashboard_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=10)

    # Add a frame for the detailed view
    detail_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
    detail_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Add buttons for different components
    components = [
        ("Health", lambda: None),  # Placeholder for health info
        ("Processor", show_processor_info),
        ("Memory", show_memory_info),
        ("Network", show_network_info),
        ("Storage", show_storage_info),
        ("GPU", show_gpu_info)
    ]

    for text, command in components:
        button = tk.Button(dashboard_frame, text=text, command=command, font=("Helvetica", 14), bg=CARD_COLOR, fg=TEXT_COLOR, borderwidth=0, width=20, height=2)
        button.pack(pady=10)

    # Display system specs in the Overview tab
    overview_display = tk.Text(detail_frame, width=70, height=20, font=("Consolas", 12), bg=CARD_COLOR, fg=TEXT_COLOR, borderwidth=0)
    overview_display.insert(tk.END, specs_text)
    overview_display.configure(state='disabled')
    overview_display.pack(pady=10)

    # Add a refresh button
    refresh_button = ttk.Button(dashboard_frame, text="Refresh", command=refresh_specs)
    refresh_button.pack(pady=20)

    # Add a close button
    close_button = ttk.Button(dashboard_frame, text="Close", command=root.quit)
    close_button.pack(pady=20)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    specs_text = get_specs()
    create_ui(specs_text)
