def total_salary(path: str) -> tuple[int, int]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            employees_lst = file.readlines()

            count_sum = 0
            for employee in employees_lst:
                info = employee.split(",")
                salary = int(info[1])
                count_sum += salary

            average = count_sum // len(employees_lst)
            return (count_sum, average)
    
    except FileNotFoundError:
        print("The File is not found!")
        return (None, None)
    except UnicodeDecodeError as e:
        print(f"The File cannot be decoded! Error: {e}")
        return (None, None)
    except Exception as e:
        print(f"Something went wrong! Error: {e}")
        return (None, None)


total, average = total_salary("salaries.txt")
print(f"The total amount of salaries: {total}, Average salary: {average}")
