print('''Hello and welcome to the \"Keep In Contact\'s!\" 
program, this program will help you keep in contact with
everybody around you.\n''')  # Welcome the user

num_contacts = 0    # Initialize the number of contacts to 0
contact_info = {}       # Initialize contact info dictionary to empty items


def main():  # Define main() function
    global num_contacts  # Specify you are using num_contacts from global scope

    num_contacts += 1   # Increment num_contacts by 1
    
    for field, _ in (('name', str),
                    ('age', int),
                    ('gender',str),
                    ('email',str),
                    ('phone number',str)):

        value = input(f'Enter contact {field} : ')
        contact_info[field] = value

    # clean the dictionary by removing brackets and quotation marks
    clean_info = str(contact_info).replace(
    '{', '').replace('}', '').replace("\'", '')
    
    # Append to file "ContactSheet.txt" as contact_file
    with open("ContactSheet.txt", "a") as contact_file:
        contact_file.write(clean_info)  # add the clean_info
        contact_file.write('\n\n')  # add two new lines

    while True:         
        more_contacts = input("Do you have more contacts? : ").lower()
        if more_contacts in {'yes', 'no'}:  # you can use also "in 'yesno'"
            break
        print("Sorry, I couldn't understand")

    if more_contacts.lower() == 'yes' and __name__ == '__main__':  # if they have more contacts and if program is being run from the same file
        main()  # run main function

if __name__ == '__main__':  # if program is being run from the same file
    main()  # run main function

print(f"Added your {num_contacts} contact(s)",
       "to a file named \"ContactSheet.txt\"") 

