c_name_list = []
c_unit_list = []
c_grade_list = []
total_unit = 0
total_grade = 0

grade_dict = {
    "A+" : 4.5,
    "A0" : 4.0, 
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
}

for _ in range(20):
    x,y,z = input().split()
    c_name_list.append(x.strip())
    c_unit_list.append(y.strip())
    c_grade_list.append(z.strip())

for name, unit, grade in zip(c_name_list, c_unit_list, c_grade_list):
    if grade == "P":
        continue
    
    total_grade += (float(unit) * grade_dict[grade])
    total_unit += float(unit)

print(total_grade/total_unit)
