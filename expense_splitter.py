#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError("Number of people must be greater than one!")
        
    if total_amount <= 0:
        raise ValueError("Total amount must be greater than zero!")
    
    flag = None #Mark by option
    while True:
        print("Please choose how to share the expense:")
        print("1. Share the expense equally")
        print("2. Share the expense unequally (custom input - split by %)")
        print("3. Exit")
        try:
            selection: int = int(input("=> Enter your number: "))
        except ValueError as e:
            print(f"Error {e}. Please enter a valid integer!!!")
            continue
        if selection == 1:
            break
        elif selection == 2:
            flag = 1
            break
        elif selection == 3:
            print("Good bye!")
            return 
        else:
            print("!!!Invalid, please select again!!!")
            continue 

    if flag: 
        sum_percentage: float = 100.00
        persons_lis = [0] * number_of_people
        i = 0 
        while i < len(persons_lis) - 1:
            try:
                person: float = float(input(f"Person {i + 1} (<= {sum_percentage:,.2f}): "))
            except ValueError as e:
                print(f"Error {e}. Please enter a valid number!!!")
                continue
            if 0 <= person <= sum_percentage:
                persons_lis[i] = person
                sum_percentage -= person
                i += 1
            else:
                print(f"The value you just entered exceeds the remaining percentage!!! ({sum_percentage:,.2f})")
                print("Please enter again!")
                continue

        persons_lis[-1] = sum_percentage
        value_lis = [total_amount * x / 100 for x in persons_lis] #list of share per person
        for j in range(len(persons_lis)):
            print(f"Person {j + 1}: ({persons_lis[j]}%) neeeds to pay {currency} {value_lis[j]:,.2f}")
        print(f"Total expenses: {currency} {total_amount:,.2f}")
        print(f"Number of people: {number_of_people}")
    else:        
        share_per_person: float = total_amount / number_of_people

        print(f"Total expenses: {currency} {total_amount:,.2f}")
        print(f"Number of people: {number_of_people}")
        print(f"Each person should pay: {currency} {share_per_person:,.2f}")
  
def main() -> None:
        try: 
            total_amount: float = float(input("Enter the total amount of the expense: "))
            number_of_people: int = int(input("Enter the number of people sharing the expense: "))
            calculate_split(total_amount, number_of_people, currency = "VND")
        except ValueError as e:
            print(f"Error {e}")
            print("Please try again with valid value!\n")

if __name__ == "__main__":
    main()

