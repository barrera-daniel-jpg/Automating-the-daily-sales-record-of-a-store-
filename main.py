from History import show_summary
from Login import product_records
# Imports the two main functions from their respective modules

print("=" * 24)  # Improves visualization and user experience
print("| WELCOME TO THE SYSTEM |")
print("=" * 24)  # Improves visualization and user experience


def request_option():
    option = input("\nAre you going to register products? (Y/N): ").upper()
    
    if option not in ['Y', 'N']:
        print("Invalid option, please try again (Y/N)")
        return request_option()
    
    return option
# Validation function: only accepts Y or N
# Any other input triggers recursion and asks again
# Returns the valid option to the while loop


while request_option() == 'Y':
    product_records()

show_summary()

print("The program has ended. Thank you for your registrations.")
# Once outside the loop, these lines execute only once
