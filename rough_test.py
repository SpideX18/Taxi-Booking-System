import tkinter as tk

def change_button_state(event):
    current_button = event.widget
    current_button.config(state="disabled")

    # Find the corresponding button in the other column of the same row
    for button in button_list:
        if str(button.grid_info()["row"]) == str(current_button.grid_info()["row"]) and \
           str(button.grid_info()["column"]) != str(current_button.grid_info()["column"]):
            button.config(state="normal")
            break

root = tk.Tk()
root.title("Buttons in Multiple Columns")

button_list = []  # List to hold all buttons

# Create buttons in two columns
for i in range(5):
    button1 = tk.Button(root, text=f"Button {i+1} (Column 1)")
    button1.grid(row=i, column=0, padx=20, pady=5)
    button1.bind("<Button-1>", change_button_state)
    button_list.append(button1)

    button2 = tk.Button(root, text=f"Button {i+1} (Column 2)")
    button2.grid(row=i, column=1, padx=20, pady=5)
    button2.config(state="disabled")  # Initially disable all buttons in column 2
    button_list.append(button2)

root.mainloop()
