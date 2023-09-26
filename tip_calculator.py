# tip_calculator.py

#This assignmet was completed with the contribution of my partners Rico, and Ephraim. 

# TODO: Create a function named calculate_tip
def tip_calculator():
    try:  #DO NOT MODIFY


    # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage

        total_cost = float(input("What is the total cost of the meal? : "))
        num_people = int(input("What is the number of people splitting the bill?"))
        tip_percentage = float(input("What is the tip percentage?"))

    
    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).


    # NOTE: Calculate the tip and tax separately. 
        tip = total_cost * tip_percentage / 100
        tax = total_cost * 0.10
        total_cost = float(total_cost + tip + tax)

    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.   
    
        bill_split = total_cost / num_people

    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00

       
       
        print(f"Total bill: ${total_cost:.2f}")
        print(f"Each person should pay: ${bill_split:.2f}")


    # NOTE: The amounts are displayed with 2 decimals only

    except ValueError: # TODO: modify this except to include a Built-in Exception
        print("Your input is invalid")
        # TODO: Print an statement telling the user their input is invalid 
    
    
if __name__ == "__main__": # DO NOT MODIFY # DO NOT MODIFY
    tip_calculator()