"""Annual Calendar created by Julianne McMillian
Purely for practice and educational purposes."""



from tkinter import *  #Allow the calendar to be created and displayed
import calendar  # Used to generate calendar
from datetime import datetime  # Used to import current year and month

now = datetime.now()  # Generates current date and time in YYYY-MM-DD format
year = now.year  # Strips 'now' variable, only leaving the current year
annuCal = calendar.calendar(year)


calendarWindowDisplay = Tk()  #Creates a new window using tkinter function
calendarWindowDisplay.geometry('550x625')  #Adjusts the size of the window
calendarWindowDisplay.title('Annual Calendar')  #Names window "Annual Calendar" as seen in top left corner; name does not override variable name
calendarHeader = Label(calendarWindowDisplay, text=(year, "CALENDAR"), bg="black", font=("Consolas 10", 28), fg='white')  #Header for the calendar, should update with new info for each passing year
calendarHeader.grid(row=1, column=1)   #Positions Calendar Header
calendarWindowDisplay.configure(background="black")  #Sets the background of the window to Black. Color chosen for aesthetic appeal
monthlyCalendarDisplay=Label(calendarWindowDisplay, text=annuCal, font="Consolas 10", fg='black')  #Creation and placement of months and days for current calendar year, set up in a grid format
monthlyCalendarDisplay.grid(row=2, column=1, padx=20)  #Positions Calendar Display
calendarWindowDisplay.mainloop()  #Keeps program open, as long as it is not closed
