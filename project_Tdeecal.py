import tkinter as tk

def calculate_tdee(): #programe calculate for eat per days (ลดน้ำหนัก)
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        # Activity levels: 
        activity_level = activity_var.get()
        activity_factors = [1.2, 1.375, 1.55, 1.725, 9]
        
        if gender_var.get() == 0:  # Male
            bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        else:  # Female
            bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        
        tdee = bmr * activity_factors[activity_level]
        
        result_label.config(text=f"ค่าของพลังงานที่ใช้กิจกรรมอื่นในแต่ละวัน (TDEE) คือ: {tdee:.2f} calories/วัน")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("TDEE Calculator")

# Labels
tk.Label(root, text="Age:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Height (cm):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Gender:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="กิจกรรมที่ทำ:").grid(row=4, column=0, padx=10, pady=5, sticky="e")

# Entries
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=10, pady=5)

# Gender buttons
gender_var = tk.IntVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value=0).grid(row=3, column=1, padx=5, pady=5, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value=1).grid(row=3, column=1, padx=5, pady=5, sticky="e")

# Activity level radio buttons
activity_var = tk.IntVar()
activity_var.set(0)  # Default to Sedentary
activities = ["ไม่ออกกำลังกาย ", "ออกกำลังกาย 1 – 2 ครั้งต่อสัปดาห์", "ออกกำลังกาย 3 – 5 ครั้งต่อสัปดาห์", "ออกกำลังกาย 6 – 7 ครั้งต่อสัปดาห์", "ออกกำลังกายทุกวัน วันละ 2 เวลา"]
for i, activity in enumerate(activities):
    tk.Radiobutton(root, text=activity, variable=activity_var, value=i).grid(row=4+i, column=1, padx=5, pady=2, sticky="w")

# Button to calculate TDEE
calculate_button = tk.Button(root, text="Calculate TDEE", command=calculate_tdee)
calculate_button.grid(row=9, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="", font=('Helvetica', 12), fg='blue')
result_label.grid(row=10, columnspan=2, padx=10, pady=5)

root.mainloop()
# %%

