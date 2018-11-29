"""
A.M.

Information extractor.

Used to pull information from the clipboard. Possible information to pull
includes: URLs, email addresses, and phone numbers. Created this script
as a means to practice regex.
"""
import re, pyperclip

url_regex = re.compile(r'''(http://|https://)?         # matching the http or https portion, if present
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


clip_board = str(pyperclip.paste())


def get_url():
    url_mo = url_regex.findall(clip_board)
    urls = [list(x) for x in url_mo]
    print('URLs extracted below:')
    for sublist in urls:
        print(end='\n')
        for x in sublist:
            print(x, end='')


def get_phone_num():
    phone_mo = phone_regex.findall(clip_board)        # running regex to find all instances of a phone number
    phone_numbers = [list(x) for x in phone_mo]       # converting list of tuples to list of lists
    print('Phone numbers extracted below:')           # telling the users that phone numbers pulled are below
    for sublist in phone_numbers:                     # for each inner-list within the outer-list
        print(end='\n')                               # print each inner-list with a newline after for readability
        for x in sublist:                             # for each string within each inner-list
           print(x, end='')                           # print out the strings side by side, surpressing the newline


def get_email_addr():
    email_mo = email_regex.findall(clip_board)
    email_addrs = [list(x) for x in email_mo]
    print('Email addresses extracted below:')
    for sublist in email_addrs:
        print(end='\n')
        for x in sublist:
            print(x, end='')


get_url()
print('\n\n\n')
get_email_addr()
print('\n\n\n')
get_phone_num()
