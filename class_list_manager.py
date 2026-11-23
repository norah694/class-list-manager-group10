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

#Written by: rawan alkahtani (task2) 
def search_name(names, name):
    for n in names:
        if n == name:
            return True
    return False

# Written by: Alya (Task 3)
def sort_names(names):
    sorted_list = sorted(names)
    return sorted_list
    
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("is Reem in the list?", search_name(names,"Reem"))
    print("Sorted names:", sort_names(names))
main()
