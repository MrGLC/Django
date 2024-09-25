import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Simple Python GUI")
    label = tk.Label(root, text="Hello, Tkinter!", padx=20, pady=20)
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()

