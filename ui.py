import tkinter as tk
from specs import get_specs

def create_ui(specs_text):
    def refresh_specs():
        new_specs = get_specs()
        specs_display.configure(state='normal')
        specs_display.delete(1.0, tk.END)
        specs_display.insert(tk.END, new_specs)
        specs_display.configure(state='disabled')

    root = tk.Tk()
    root.title("PC Specs")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")

    title_label = tk.Label(root, text="Your PC Specifications", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
    title_label.pack(pady=10)

    specs_display = tk.Text(root, width=50, height=10, font=("Consolas", 10), bg="#ffffff", borderwidth=0)
    specs_display.insert(tk.END, specs_text)
    specs_display.configure(state='disabled')
    specs_display.pack(pady=10)

    refresh_button = tk.Button(root, text="Refresh", command=refresh_specs)
    refresh_button.pack(pady=10)

    root.mainloop()