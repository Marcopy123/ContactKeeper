print('''Hello and welcome to the \"Keep In Contact\'s!\" 
program, this program will help you keep in contact with
everybody around you. ''')  # Welcome the user

num_contacts = 0    # Initialize the number of contacts to 0
contact_info = {"Name" : None, 
                "Age" : None,
                "Gender" : None,
                "Email" : None,
                "Phone #" : None
                }       # Initialize contact info dictionary to empty values


def main():  # Define main() function
    global num_contacts  # Specify you are using num_contacts from global scope

    num_contacts += 1   # Increment num_contacts by 1
    name = input("\nAdd a name : ") # Ask for name
    age = input("Add an age : ")    # Ask for age
    gender = input("Add their gender : ")   # Ask for gender
    email = input("Add their email : ")     # Ask for email
    phone_number = input("Add their phone number : ")   # Ask for phone number
    
    # assign name variable to value of key name in contact_info dictionary
    contact_info['Name'] = name 
    # assign age variable to value of key Age in contact_info dictionary
    contact_info['Age'] = age 
    # assign gender variable to value of key Gender in contact_info dictionary
    contact_info['Gender'] = gender
    # assign email variable to value of key Email in contact_info dictionary
    contact_info['Email'] = email
    # assign phone_number variable to value of key Phone # in contact_info dictionary
    contact_info['Phone #'] = phone_number

    # clean the dictionary by removing brackets and quotation marks
    clean_info = str(contact_info).replace(
    '{', '').replace('}', '').replace("\'", '')
    
    # Append to file "ContactSheet.txt" as contact_file
    with open("ContactSheet.txt", "a") as contact_file:
        contact_file.write(clean_info)  # add the clean_info
        contact_file.write('\n\n')  # add two new lines

    more_contacts = input("Do you have more contacts? : ")  # ask if they have more contacts

    while more_contacts.lower() != 'yes' and more_contacts.lower() != 'no': # if they did not answer yes or no
        print("Sorry, I couldn't understand")   
        more_contacts = input("Do you have more contacts? : ")  # ask if they have more contacts

    if more_contacts.lower() == 'yes':  # if they have more contacts
        if __name__ == '__main__':  # if program is being run from the same file
            main()  # run main function

if __name__ == '__main__':  # if program is being run from the same file
    main()  # run main function

print(f"Added your {num_contacts} contact(s)",
       "to a file named \"ContactSheet.txt\"") 

