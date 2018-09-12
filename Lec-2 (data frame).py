import pandas as pd


data = {
    "student": ["AJ", "Mark", "Bob", "Rachel", "Steven"],
    "Math": [98, 50, 23, 72, 87],
    "science": [96, 45, 76, 54, 1],
    "Sport": ["Basketball", "Swimming", "TT", "Badminton", "Tae Kwan Do"]
}
students = pd.DataFrame(data, columns=["student", "Math", "science", "Sport"])
print(students)
