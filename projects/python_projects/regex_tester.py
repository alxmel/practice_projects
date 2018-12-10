"""
A.M.

Information extractor.

Used to pull information from the clipboard. Possible information to pull
includes: URLs, email addresses, and phone numbers. Created this script
as a means to practice regex.

***Updated to also include the option to read in a file and extract
URLs, email addresses, and phone numbers from the specified file.
"""
import re, pyperclip, os

url_regex = re.compile(r'''(http://|https://)+         # matching the http or https portion, if present
                         (www\.|www\d\.)?              # Matching the 'www' portion of the string, optional
                         ([a-z]*\.)?                   # host, optional
                         ([a-zA-Z0-9]+)                # website
                         (\.)+                         # the dot separator
                         (\w{2,3})+                    # .com, .net, etc.
                         ([a-z0-9/:.]*)?               # path or port number after
                         ''', re.VERBOSE)

email_regex = re.compile(r'''([a-zA-Z0-9.\-_$%]+)    # Matching the email address
                         (@)+                            # @ sign separator
                         ([a-zA-Z0-9]+)                # domain name
                         (\.)+                            # dot separator
                         (\w{2,3})                     # .com, .net, .edu, etc.
                         ''', re.VERBOSE | re.I)

phone_regex = re.compile(r'''
                         (\+1\s)?                      # +1 at the beginning, optional
                         (\(\d{3}\)|\d{3})?            # area code optional
                         (\s|\.|\-)?                   # phone number separators, optional
                         (\d{3})                       # first three digits
                         (\s|\.|\-)?                   # phone number separator again, optional
                         (\d{4})                       # final four digits
                         (\s*(ext|x|ext.)\s*\d{2,5})?  # extension, optional
                         ''', re.VERBOSE | re.I)



# Function for obtaining URLs from clipboard.
def get_url(clip_paste):
    url_mo = url_regex.findall(clip_paste)
    urls = [list(x) for x in url_mo]
    print('URLs extracted below:')
    for sublist in urls:
        print(end='\n')
        for x in sublist:
            print(x, end='')

# Function for extracting phone numbers from clipboard.
def get_phone_num(clip_paste):
    phone_mo = phone_regex.findall(clip_paste)        # running regex to find all instances of a phone number
    phone_numbers = [list(x) for x in phone_mo]       # converting list of tuples to list of lists
    print('Phone numbers extracted below:')           # telling the users that phone numbers pulled are below
    for sublist in phone_numbers:                     # for each inner-list within the outer-list
        print(end='\n')                               # print each inner-list with a newline after for readability
        for x in sublist:                             # for each string within each inner-list
           print(x, end='')                           # print out the strings side by side, surpressing the newline

# Function for extracting email addresses from clipboard.
def get_email_addr(clip_paste):
    email_mo = email_regex.findall(clip_paste)
    email_addrs = [list(x) for x in email_mo]
    print('Email addresses extracted below:')
    for sublist in email_addrs:
        print(end='\n')
        for x in sublist:
            print(x, end='')

# Function for extracting URLs from a file
def get_url_file(file_name):
    url_file_mo = url_regex.findall(file_name)
    urls_from_file = [list(x) for x in url_file_mo]
    print('URLs extracted from the file provided below:')
    for sublist in urls_from_file:
        print(end='\n')
        for x in sublist:
            print(x, end='')

# Function for extracting phone numbers from a file
def get_phone_num_file(file_name):
    phone_file_mo = phone_regex.findall(file_name)
    phones_from_file = [list(x) for x in phone_file_mo]
    print('Phone numbers extracted from the file provided below:')
    for sublist in phones_from_file:
        print(end='\n')
        for x in sublist:
            print(x, end='')

# Function for extracting email addresses from a file
def get_email_addr_file(file_name):
    email_file_mo = email_regex.findall(file_name)
    emails_from_file = [list(x) for x in email_file_mo]
    print('emails addresses extracted from the file provided below:')
    for sublist in emails_from_file:
        print(end='\n')
        for x in sublist:
            print(x, end='')





# While loop asking for input to determine whether to use clipboard or provide a file
while True:
    print('Hello! Welcome to the URL/email/phone number extractor!')
    print('\nPlease enter "c" for extracting from your clipboard, "f" for extracting from a file, or "exit" to exit: ')
    user_choice = input()
    if user_choice.lower() == 'c':
        clip_board = str(pyperclip.paste())
        get_url(clip_board)
        print('\n\n\n')
        get_email_addr(clip_board)
        print('\n\n\n')
        get_phone_num(clip_board)
        print('\n\n\n')
        break
    elif user_choice == 'f':
        print('\nIf the file is located in ' + os.getcwd() + ' then enter just the filename. Otherwise provide the full path to the file: ')
        file_location = input()
        file_extract = open(file_location, 'r')
        file_read = file_extract.read()
        print('\n')
        get_phone_num_file(file_read)
        print('\n\n\n')
        get_email_addr_file(file_read)
        print('\n\n\n')
        get_url_file(file_read)
        print('\n\n\n')
        break
    elif user_choice.lower() == 'exit':
        break
    else:
        print('\nSorry, input did not match any of the options. Please try again.')
        continue
