import tkinter as tk

def draw_shapes(canvas):

    canvas.create_rectangle(50, 50, 150, 100, fill="yellow")

    canvas.create_oval(200, 50, 300, 150, fill="green")

    canvas.create_line(350, 50, 450, 100, fill="red")

if __name__ == "__main__":

    root = tk.Tk()

    root.title("Graphic Model with Tkinter")

    canvas = tk.Canvas(root, width=500, height=200)

    canvas.pack()

    draw_shapes(canvas)

    root.mainloop()