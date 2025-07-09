import tkinter as tk
from tkinter import Canvas, messagebox
import math
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import io

def calculate_resultant():
    try:
        angle = float(entry_angle.get())
        weight1 = float(entry_weight1.get())
        weight2 = float(entry_weight2.get())
        resultant_force = math.sqrt(weight1**2 + weight2**2 - 2 * weight1 * weight2 * math.cos(math.radians(angle)))
        label_result.config(text=f"Resultant Force: {resultant_force:.2f} N")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for weights and angle.")

# def render_latex(formula):
    #     fig, ax = plt.subplots()
    #     ax.text(0.5, 0.5, f"${formula}$", fontsize=5, color='white', style='italic', ha='center', va='center')
    #     ax.axis('off')
    #     buf = io.BytesIO()
    #     plt.savefig(buf, format='png', bbox_inches='tight', transparent=True, dpi=200, pad_inches=0, facecolor='none')
    #     buf.seek(0)
    #     img = Image.open(buf)
    #     return ImageTk.PhotoImage(img)

# gui window      
root = tk.Tk()
root.title("Gravesande's Apparatus Simulation")
root.attributes('-fullscreen', True)
root.configure(bg="#2c2f33")

font_style = ("Helvetica", 14, "bold")

def enable_drawing():
    global drawing
    drawing = not drawing

def draw(event):
    if drawing:
        canvas.create_line(event.x, event.y, event.x+1, event.y+1, fill='white', width=2, tags=('user_drawn',))

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="#23272a", highlightthickness=0)
canvas_width = root.winfo_screenwidth()
canvas_height = root.winfo_screenheight()
canvas.pack()
canvas.bind('<B1-Motion>', draw)
drawing = False

# pulle
canvas.create_oval(canvas_width*0.35, canvas_height*0.1, canvas_width*0.4, canvas_height*0.15, outline="white", fill="gray", width=5)
canvas.create_oval(canvas_width*0.6, canvas_height*0.1, canvas_width*0.65, canvas_height*0.15, outline="white", fill="gray", width=5)

canvas.create_text(canvas_width*0.5, canvas_height*0.65, text="C", font=font_style, fill="white", anchor='center')

canvas.create_line(canvas_width*0.37, canvas_height*0.15, canvas_width*0.37, canvas_height*0.75, fill="white", width=6)
canvas.create_line(canvas_width*0.63, canvas_height*0.15, canvas_width*0.63, canvas_height*0.75, fill="white", width=6)
canvas.create_line(canvas_width*0.37, canvas_height*0.15, canvas_width*0.5, canvas_height*0.8, fill="white", width=4)
canvas.create_line(canvas_width*0.63, canvas_height*0.15, canvas_width*0.5, canvas_height*0.8, fill="white", width=4)

# Draw the weights
canvas.create_rectangle(canvas_width*0.36, canvas_height*0.75, canvas_width*0.40, canvas_height*0.85, fill="gray", outline="white")
canvas.create_rectangle(canvas_width*0.60, canvas_height*0.75, canvas_width*0.64, canvas_height*0.85, fill="gray", outline="white")
canvas.create_rectangle(canvas_width*0.45, canvas_height*0.8, canvas_width*0.55, canvas_height*0.9, fill="gray", outline="white")

# Label the weights and inputs
canvas.create_text(canvas_width*0.38, canvas_height*0.80, text="F1", font=font_style, fill="white", anchor='center')
canvas.create_text(canvas_width*0.62, canvas_height*0.80, text="F3", font=font_style, fill="white", anchor='center')
canvas.create_text(canvas_width*0.5, canvas_height*0.87, text="Fm", font=font_style, fill="white", anchor='center')


tk.Label(root, text="Enter Weight 1 (N):", font=font_style, fg="white", bg="#2c2f33").place(x=50, y=100)
entry_weight1 = tk.Entry(root, font=font_style, bg="#2c2f33", fg="white", insertbackground="white", highlightbackground="#2c2f33", highlightcolor="#7289da")
entry_weight1.place(x=50, y=130, width=200, height=40)

tk.Label(root, text="Enter Weight 2 (N):", font=font_style, fg="white", bg="#2c2f33").place(x=50, y=180)
entry_weight2 = tk.Entry(root, font=font_style, bg="#2c2f33", fg="white", insertbackground="white", highlightbackground="#2c2f33", highlightcolor="#7289da")
entry_weight2.place(x=50, y=210, width=200, height=40)

tk.Label(root, text="Enter Angle (degrees):", font=font_style, fg="white", bg="#2c2f33").place(x=50, y=260)
entry_angle = tk.Entry(root, font=font_style, bg="#2c2f33", fg="white", insertbackground="white", highlightbackground="#2c2f33", highlightcolor="#7289da")
entry_angle.place(x=50, y=290, width=200, height=40)

# latex formula (doesnt work)
latex_formula = "R = \sqrt{F_1^2 + F_2^2 - 2F_1F_2 cosC}"

# eqn_image = render_latex(latex_formula)
# eqn_label = tk.Label(root, image=eqn_image, bg="#2c2f33")
# eqn_label.image = eqn_image
# eqn_label.place(x=50, y=350, anchor='nw')

btn_calculate = tk.Button(root, text="Calculate Resultant", font=font_style, bg="#7289da", fg="white", command=calculate_resultant)
btn_calculate.place(relx=0.05, rely=0.5, anchor='w')

label_result = tk.Label(root, text="Resultant Force: ", font=font_style, fg="white", bg="#2c2f33")
label_result.place(relx=0.05, rely=0.55, anchor='w')

btn_draw = tk.Button(root, text="Draw", font=font_style, bg="#7289da", fg="white", command=enable_drawing)
btn_draw.place(relx=0.95, rely=0.05, anchor='ne')

def clear_canvas():
    for item in canvas.find_all():
        if 'user_drawn' in canvas.gettags(item):
            canvas.delete(item)

btn_erase = tk.Button(root, text="Erase", font=font_style, bg="#ff4d4d", fg="white", command=clear_canvas)
btn_erase.place(relx=0.90, rely=0.05, anchor='ne')

root.mainloop()
