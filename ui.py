import tkinter as tk
from tkinter import ttk
from specs import get_specs
import psutil

def get_network_info():
    net_io = psutil.net_io_counters()
    network_info = f"Bytes Sent: {net_io.bytes_sent}\n"
    network_info += f"Bytes Received: {net_io.bytes_recv}\n"
    network_info += f"Packets Sent: {net_io.packets_sent}\n"
    network_info += f"Packets Received: {net_io.packets_recv}\n"
    return network_info

def show_network_info():
    network_info = get_network_info()
    detail_frame.pack_forget()
    detail_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    for widget in detail_frame.winfo_children():
        widget.destroy()

    network_label = tk.Label(detail_frame, text="Network Information", font=("Helvetica", 14, "bold"), bg="#2e2e2e", fg="#ffffff")
    network_label.pack(pady=10)

    network_display = tk.Text(detail_frame, width=50, height=10, font=("Consolas", 10), bg="#1e1e1e", fg="#ffffff", borderwidth=0)
    network_display.insert(tk.END, network_info)
    network_display.configure(state='disabled')
    network_display.pack(pady=10)

def show_processor_info():
    # Placeholder function for processor information
    detail_frame.pack_forget()
    detail_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    for widget in detail_frame.winfo_children():
        widget.destroy()

    processor_label = tk.Label(detail_frame, text="Processor Information", font=("Helvetica", 14, "bold"), bg="#2e2e2e", fg="#ffffff")
    processor_label.pack(pady=10)

    processor_display = tk.Text(detail_frame, width=50, height=10, font=("Consolas", 10), bg="#1e1e1e", fg="#ffffff", borderwidth=0)
    processor_display.insert(tk.END, "Processor details go here...")
    processor_display.configure(state='disabled')
    processor_display.pack(pady=10)

def show_memory_info():
    # Placeholder function for memory information
    detail_frame.pack_forget()
    detail_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    for widget in detail_frame.winfo_children():
        widget.destroy()

    memory_label = tk.Label(detail_frame, text="Memory Information", font=("Helvetica", 14, "bold"), bg="#2e2e2e", fg="#ffffff")
    memory_label.pack(pady=10)

    memory_display = tk.Text(detail_frame, width=50, height=10, font=("Consolas", 10), bg="#1e1e1e", fg="#ffffff", borderwidth=0)
    memory_display.insert(tk.END, "Memory details go here...")
    memory_display.configure(state='disabled')
    memory_display.pack(pady=10)

def show_storage_info():
    # Placeholder function for storage information
    detail_frame.pack_forget()
    detail_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    for widget in detail_frame.winfo_children():
        widget.destroy()

    storage_label = tk.Label(detail_frame, text="Storage Information", font=("Helvetica", 14, "bold"), bg="#2e2e2e", fg="#ffffff")
    storage_label.pack(pady=10)

    storage_display = tk.Text(detail_frame, width=50, height=10, font=("Consolas", 10), bg="#1e1e1e", fg="#ffffff", borderwidth=0)
    storage_display.insert(tk.END, "Storage details go here...")
    storage_display.configure(state='disabled')
    storage_display.pack(pady=10)

def create_ui(specs_text):
    def refresh_specs():
        try:
            new_specs = get_specs()
            specs_display.configure(state='normal')
            specs_display.delete(1.0, tk.END)
            specs_display.insert(tk.END, new_specs)
            specs_display.configure(state='disabled')
        except Exception as e:
            specs_display.configure(state='normal')
            specs_display.delete(1.0, tk.END)
            specs_display.insert(tk.END, f"An error occurred while refreshing specs: {e}")
            specs_display.configure(state='disabled')

    global root, detail_frame
    root = tk.Tk()
    root.title("PC Specs")
    root.geometry("1000x600")
    root.configure(bg="#2e2e2e")

    # Add a title label
    title_label = tk.Label(root, text="Your PC Specifications", font=("Helvetica", 18, "bold"), bg="#2e2e2e", fg="#ffffff")
    title_label.pack(pady=20)

    # Add a frame for the main dashboard
    dashboard_frame = tk.Frame(root, bg="#2e2e2e")
    dashboard_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=10)

    # Add a frame for the detailed view
    detail_frame = tk.Frame(root, bg="#2e2e2e")
    detail_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Add buttons for different components
    components = [
        ("Health", lambda: None),  # Placeholder for health info
        ("Processor", show_processor_info),
        ("Memory", show_memory_info),
        ("Network", show_network_info),
        ("Storage", show_storage_info)
    ]

    for text, command in components:
        button = tk.Button(dashboard_frame, text=text, command=command, font=("Helvetica", 14), bg="#1e1e1e", fg="#ffffff", borderwidth=0, width=20, height=2)
        button.pack(pady=10)

    # Add a text widget to display the specs
    specs_display = tk.Text(dashboard_frame, width=30, height=15, font=("Consolas", 12), bg="#1e1e1e", fg="#ffffff", borderwidth=0)
    specs_display.insert(tk.END, specs_text)
    specs_display.configure(state='disabled')
    specs_display.pack(pady=10)

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