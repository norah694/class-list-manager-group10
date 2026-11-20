# Class List Manager - Group 10
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====
# Written by: norah albassam (Task 1)

def count_names(names):
    count = 0

    for name in names:
        count += 1

    return count


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)

    print("Number of names:", count_names(names))

main()
