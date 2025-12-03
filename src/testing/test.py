import tkinter as tk
from tkinter import messagebox

# Here is the login screen that checks if the login works
#Hard coded username and password just to try and test
def fake_login(username, password):
    if username == "admin" and password == "1234":
        return {"status": "success", "token": "abcd1234xyz"}
    else:
        return {"status": "error", "message": "Invalid credentials"}

# Here is the actualy logining
def login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    # Validators it makes sure that everything is here
    if not username or not password:
        messagebox.showwarning("Validation Error", "All fields are required.")
        return

    #We get the response from the login and make sure that everything works
    response = fake_login(username, password)

    #What to do if everything works
    if response["status"] == "success":
        messagebox.showinfo("Login Success", "Welcome!")
        root.destroy()
        open_dashboard(response["token"])
    else: #If the login fails
        messagebox.showerror("Login Failed", response["message"])

# Here is the actualy login screen that pops up
root = tk.Tk()
root.title("Payroll Login")
root.geometry("320x200")
root.resizable(False, False)

tk.Label(root, text="Username:", font=("Arial", 12)).pack(pady=5)
entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

tk.Label(root, text="Password:", font=("Arial", 12)).pack(pady=5)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

tk.Button(root, text="Login", width=15, bg="lightblue", command=login).pack(pady=15)

root.mainloop()


