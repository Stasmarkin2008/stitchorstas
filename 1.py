import customtkinter as ctk

ctk.set_appearance_mode("dark")

root = ctk.CTk()  
root.title("Менеджер целей")
root.geometry("1000x600")

scroll_frame = ctk.CTkScrollableFrame(root)
scroll_frame.pack(fill="both", expand=True, padx=20, pady=(20, 80))

def button_event():
    entry = ctk.CTkEntry(scroll_frame, placeholder_text="Введите цель...", width=300)
    entry.pack(pady=5, padx=10, anchor="w")
    entry.focus()

    def create_checkbox(event=None):
        goal_text = entry.get().strip()
        
        if goal_text:
            entry.destroy()
            
            check_var = ctk.StringVar(value="off")
            
            def checkbox_event():
                if check_var.get() == "on":
                    checkbox.destroy()

            checkbox = ctk.CTkCheckBox(
                scroll_frame, 
                text=goal_text, 
                command=checkbox_event,
                variable=check_var, 
                onvalue="on", 
                offvalue="off"
            )
            checkbox.pack(pady=5, padx=10, anchor="w")
        else:
            entry.destroy() 

    entry.bind("<Return>", create_checkbox)


button = ctk.CTkButton(
    root, 
    text="+", 
    width=50, 
    height=50, 
    font=("Arial", 24, "bold"),
    corner_radius=25,
    command=button_event
)
button.place(relx=1.0, rely=1.0, x=-30, y=-30, anchor="se")

root.mainloop()