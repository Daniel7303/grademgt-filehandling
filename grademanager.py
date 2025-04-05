class Students:
    def __init__(self, name="", grade=0, std_details=None):
        if std_details is None:
            std_details = []
        self.name = name
        self.grade = grade
        self.std_details = std_details

    def std_grade(self):
        if 90 <= self.grade <= 100:
            return "A"
        elif 80 <= self.grade <= 89:
            return "B"
        elif 70 <= self.grade <= 79:
            return "C"
        elif 60 <= self.grade <= 69:
            return "D"
        elif self.grade < 60:
            return "F"
        else:
            return "Invalid grade"

    def submit(self):
        self.name = input("Enter student name: ").strip()
        while True:
            if not self.name:
                print("name must not be emtpy")
                continue
            try:
                self.grade = int(input("Enter student Grade: "))
            except ValueError:
                print("Invalid input for grade. Please enter a number.")
                continue

            self.std_details.append((self.name, self.grade, self.std_grade()))

            cont = input("Enter Y/N:  ").upper()
            if cont != "Y":
                break

        print(f"Student Name Score  Grade ")
        with open("Student.txt", "w") as file:
            total = 0
            file.write(f"{'Student Name':<15}{'Score':<8}{'Grade'} \n")
            file.write("-" * 30 + "\n")
            for detail in self.std_details:
                total += detail[1]
                avg = total / 2
                print(f"{detail[0]:<15}{detail[1]:<8}{detail[2]}")
                file.write(f"{detail[0]:<15}{detail[1]:<8}{detail[2]} \n")

            file.write(f"{'Total':<15}{total:<8}\n")
            file.write(f"{'Average':<15}{avg:<8}\n")
            print(f"{'Total':<15}{total:<8}\n")
            print(f"{'Average':<15}{avg:<8}\n")

        with open("Student.txt", 'r') as f:
            content = f.read()
            print(content)



if __name__ == "__main__":
    student = Students()
    student.submit()
