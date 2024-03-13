import calendar  #The Calendar function is used to derive the monthName from month.
from datetime import datetime  #Datetime function is used to get current date for user's journal entry.
import os

now = datetime.now()  #Imports date in YYYY/MM/DD [HH:MM:SS] format. Hours, minutes, and seconds are not used.
year = now.year  #Grabs current year from datetime
month = now.month  #Grabs current month from datetime
day = now.day  #Grabs current day from datetime
monthName = calendar.month_name[month]  #The actual name of the month, obtained from the month variable (e.g. 3 = "March"
journalHeader = str(monthName) + " " + str(day) + " " + str(year)  #Converts any varying type into string

file_name = 'DailyJournalEntries.txt'  #User entries will be stored here.
active = True

quitJournal = "q"  #If the user enters 'q' or 'Q' the program will quit, and be stored in DailyJournalEntries.txt
dailyJournal = ''  #User input will be stored in this variable

print(journalHeader)  #Creates the header and title for the console
print("How are you today? Press 'Q' to quit.")

with open(file_name, "a") as f:  #Prints the header and prompt into DailyJournalEntries.txt
    print(journalHeader, file=f)
    print("How are you today?\n", file=f)

while active:
    dailyJournal = input("\n\t")  #User inputs how their day went, and any problems they may face
    if dailyJournal == ("q" or "Q"):  #If user enters "q" or "Q" in the console, program will quit and information will be stored in DailyJournalEntries.txt
        break
    with open(file_name, "a") as f:  #Writes user entry into file
        f.write(dailyJournal)

with open(file_name, "a") as f:  #Closes the prompt
    f.write("\n\nThanks for talking, see you later!\n\n")
    f.write("~"*30)
    f.write("\n")

os.system(file_name)