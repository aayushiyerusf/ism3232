# hello_ism3232.py
# Author: Aayush Iyer

# --- What happened when I ran this script? ---
# 1. The shell found the python3 interpreter at: /opt/homebrew/bin/python3
# 2. Python read the file from top to bottom: True
# 3. The f-string on line 15 evaluated {weekly_hours} to: 6
# 4. The output appeared in: the terminal

print("Hello, ISM 3232!")
course_name = 'Business Application Development'
credit_hours = 3
weekly_hours = credit_hours * 2
print(f'Course: {course_name}')
print(f'Expected weekly hours: {weekly_hours}')
print('Environment verified. Week 1 complete.')

