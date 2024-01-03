import tkinter as tk

# Function to remove small brackets from dictionary values
def remove_brackets():
    original_list = [(1,), (2,), (3,), (4,)]
    modified_list = [item[0] for item in original_list]
    
    print(modified_list)

# Creating a tkinter window
root = tk.Tk()
root.title("Remove Brackets from Dictionary")

# Creating a label to display the result
result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.pack(padx=20, pady=10)

# Creating a button to trigger the function
remove_brackets_button = tk.Button(root, text="Remove Brackets", command=remove_brackets)
remove_brackets_button.pack(pady=10)

# Running the tkinter main loop
root.mainloop()
