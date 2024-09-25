from tkinter import *

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Create the three poles
        self.pole_a = Label(self, text="Pole A")
        self.pole_a.grid(row=0, column=0, sticky=W)
        self.pole_b = Label(self, text="Pole B")
        self.pole_b.grid(row=2, column=0, sticky=W)
        self.pole_c = Label(self, text="Pole C")
        self.pole_c.grid(row=4, column=0, sticky=W)

        # Create the disks
        self.disks = []
        for i in range(1, 8):
            disk = Label(self, text=f"Disk {i}", bg="grey")
            disk.grid(row=i, column=1, sticky=W)
            self.disks.append(disk)

        # Create the buttons
        self.start_button = Button(self, text="Start", command=self.start_game)
        self.start_button.grid(row=9, column=0, sticky=W)
        self.step_button = Button(self, text="Step", command=self.step_through_game)
        self.step_button.grid(row=9, column=1, sticky=W)

    def start_game(self):
        move_disks(3, "A", "B", "C")

    def step_through_game(self):
        pass

    # Function to animate the movement of a disk
    def move_disk(self, disk, pole):
        disk.config(bg="red")
        self.update_idletasks()
        self.after(1000)
        disk.config(bg="grey")
        self.update_idletasks()
        self.after(1000)
        pole.config(text=f"{self.pole_a.cget('text')} {self.pole_b.cget('text')} {self.pole_c.cget('text')}")

def move_disks(n, source, auxiliary, target, master):
    # Base case: if the number of disks is 0, do nothing
    if n == 0:
        return

    # Step 1: Move n-1 disks from source to auxiliary
    # This is represented in the GUI by animating the movement of disks from pole A to pole B
    for i in range(n):
        master.move_disk(master.disks[i], master.pole_b)
    move_disks(n - 1, source, target, auxiliary, master)

    # Step 2: Move the largest disk from source to target
    # This is represented in the GUI by animating the movement of disk n from pole A to pole C
    master.move_disk(master.disks[-1], master.pole_c)

    # Step 3: Move n-1 disks moved earlier to target
    # This is represented in the GUI by animating the movement of disks from pole B to pole C
    for i in range(n):
        master.move_disk(master.disks[i], master.pole_c)

def play_hanoi(master):
    print(f"The least possible number of moves to move {n} disks from source 'A' pole to target 'C' pole is {(2**n)-1}.")
    print("The below setup for the tower will be used:\n"
          "A is source, C is target, B is auxiliary")
    play = input("Press 'y' to play the game: ").lower()
    if play == 'y':
        master.start_game()
    else:
        master.step_through_game()

# Create the window
root = Tk()
root.title("Tower of Hanoi")

# Create an instance of the App class
app = App(root)

# Play the game
play_hanoi(app)

# Start the event loop
root.mainloop()
