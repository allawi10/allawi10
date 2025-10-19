def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    try:
        n = int(input("Enter number of students: "))
        if n <= 0:
            print("Number must be positive.")
            return
    except ValueError:
        print("Invalid number.")
        return

    grades = []
    for i in range(n):
        while True:
            try:
                grade = float(input(f"Enter grade for student {i+1}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input, enter a number.")

    # Average
    avg = sum(grades) / n
    avg_letter = get_letter_grade(avg)

    # Count each letter
    letters = [get_letter_grade(g) for g in grades]
    counts = {l: letters.count(l) for l in "ABCDF"}

    print("\n--- Results ---")
    print(f"Class Average: {avg:.2f} ({avg_letter})")
    print("Grade counts:")
    for letter, count in counts.items():
        print(f"{letter}: {count}")

if name == "main":
    main()
