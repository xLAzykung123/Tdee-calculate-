import tkinter as t
from tkinter import messagebox

def calculate_tdee():
    try:
        age = int(entry_age.get())
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        activity_level = activity_var.get()
        activity_factors = [1.2, 1.375, 1.55, 1.725, 9]

        if gender_var.get() == 0:  # Male
            bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        else:  # Female
            bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

        tdee = bmr * activity_factors[activity_level]

        messagebox.showinfo("TDEE Result", f"ค่า TDEE ของคุณคือ: {tdee:.2f} แคลอรี่/วัน")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

win = t.Tk()
win.title("TDEE Calculator")
win.geometry("480x580")
win.configure(bg="#FFCCCC")

name_label = t.Label(text="TDEE CALCULATE", bg="yellow", fg="red", font=("Cordia New", 15, "bold", "italic"))
name_label.pack()

label_age = t.Label(win, text="Age:", bg="#CCFFFF", fg="#444444", font=("Cordia New", 15, "bold"))
label_age.pack()

entry_age = t.Entry(win, font=("Cordia New", 15, "bold", "underline"))
entry_age.pack()

label_weight = t.Label(win, text="Weight (kg):", bg="#CCFFFF", fg="#444444", font=("Cordia New", 15, "bold"))
label_weight.pack()

entry_weight = t.Entry(win, font=("Cordia New", 15, "bold", "underline"))
entry_weight.pack()

label_height = t.Label(win, text="Height (cm):", bg="#CCFFFF", fg="#444444", font=("Cordia New", 15, "bold"))
label_height.pack()

entry_height = t.Entry(win, font=("Cordia New", 15, "bold", "underline"))
entry_height.pack()

label_gender = t.Label(win, text="Gender:", bg="#CCFFFF", fg="#444444", font=("Cordia New", 15, "bold"))
label_gender.pack()

gender_var = t.IntVar()
male_radio = t.Radiobutton(win, text="Male", variable=gender_var, value=0, bg="#DDDDDD", font=("Cordia New", 15, "bold", "underline"))
male_radio.pack()
female_radio = t.Radiobutton(win, text="Female", variable=gender_var, value=1, bg="#DDDDDD", font=("Cordia New", 15, "bold", "underline"))
female_radio.pack()

label_activity = t.Label(win, text="Activity Level:", bg="#CCFFFF", fg="#444444", font=("Cordia New", 15, "bold", "underline"))
label_activity.pack()

activity_var = t.IntVar()
activity_var.set(0)  

activity_option1 = "Sedentary"
activity_option2 = "Lightly active (exercise 1-2 days/week)"
activity_option3 = "Moderately active (exercise 3-5 days/week)"
activity_option4 = "Very active (exercise 6-7 days/week)"
activity_option5 = "Super active (exercise 2 times/day)"

t.Radiobutton(win, text=activity_option1, variable=activity_var, value=0, bg="#DDDDDD", font=("Cordia New", 15, "bold", "underline")).pack()
t.Radiobutton(win, text=activity_option2, variable=activity_var, value=1, bg="#DDDDDD", font=("Cordia New", 15, "bold", "underline")).pack()
t.Radiobutton(win, text=activity_option3, variable=activity_var, value=2, bg="#DDDDDD", font=("Cordia New", 15, "bold", "underline")).pack()
t.Radiobutton(win, text=activity_option4, variable=activity_var, value=3, bg="#DDDDDD", font=("Cordia New", 15, "bold", "underline")).pack()
t.Radiobutton(win, text=activity_option5, variable=activity_var, value=4, bg="#DDDDDD", font=("Cordia New", 15, "bold", "underline")).pack()

calculate_button = t.Button(win, text="Calculate TDEE", command=calculate_tdee, bg="#0033FF", fg="#FFFFFF", font=("Cordia New", 15, "bold"))
calculate_button.pack()

win.mainloop()
