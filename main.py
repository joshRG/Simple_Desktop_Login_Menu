import customtkinter

customtkinter.set_appearance_mode("system") 
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1920×1080")

def login():
    UserEntry.delete(0, -1)
    PasswordEntry.delete(0, -1)
    print("You're logged in.")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

UserEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
UserEntry.pack(pady=12, padx=10)

PasswordEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
PasswordEntry.pack(pady=12, padx=10)

SubmitButton = customtkinter.CTkButton(master=frame, text="Login", command=login)
SubmitButton.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()