# to sort alphabetically, either store in set, or compare ascii of each letter, if same for all, leave then go to second
# letter, else if same only partial, sort based on size, then go to second for same ascii
# actually, when you think of it...the lower the sum, means they come b4 . no?? so normal comparision should do mj

# forget that, python compares strings logically char by char
# alphabetically using each unicode value , setting smaller as needed
# https://www.journaldev.com/23511/python-string-comparison#:~:text=Python%20string%20comparison%20is%20performed,their%20Unicode%20value%20is%20compared.
# this has more info
# ord() shows unicode of chars too
# greater string is considered longer if both have the same characters till end of smaller string
# python is logical!
