"""
set_clock.py

Author: Cole Vikupitz
Last Modified: 11/21/2017
"""

# Imports
from tkinter import *       # Use to make GUI
import sound                # sound.py accompanies this file


# Window class that displays the timer
class ClockWindow:

    # Sounds for the introduction message, help messages, etc.
    misc_path = "wav_files_provided/miscellaneous_f/"
    YOU_SELECTED_WAV = misc_path + "you_selected_f.wav"
    # Sounds for announcing the system's current state; set the weekday, hour, minute, etc.
    SET_WEEKDAY_WAV = misc_path + "Set_day_of_week_f.wav"
    SET_HOUR_WAV = misc_path + "Set_hour_f.wav"
    SET_MINUTE = misc_path + "Set_minute_f.wav"
    #SET_AM_PM = misc_path + "set_am_pm.wav"

    # Keep a list of sounds used for the weekdays for easier use
    # Indexed access: 0 for Sunday, 1 for Monday, ..., 5 for Friday, 6 for Saturday
    weekday_path = "wav_files_provided/days_of_week_f/"
    WEEKDAYS_WAV = [weekday_path + "sunday_f.wav",
                    weekday_path + "monday_f.wav",
                    weekday_path + "tuesday_f.wav",
                    weekday_path + "wednesday_f.wav",
                    weekday_path + "thursday_f.wav",
                    weekday_path + "friday_f.wav",
                    weekday_path + "saturday_f.wav"]

    # Keep global for time directory for simpler access to sound files
    TIME_WAV_DIR = "wav_files_provided/numbers_f/"
    # Sound files for AM, PM, O 'clock, etc.
    OH_WAV = TIME_WAV_DIR + "oh_f.wav"
    AM_WAV = TIME_WAV_DIR + "AM_f.wav"
    PM_WAV = TIME_WAV_DIR + "PM_f.wav"
    OH_CLOCK_WAV = TIME_WAV_DIR + "o_clock_f.wav"

    TMP_FILE_WAV = "tmp_file_p782s8u.wav" # Random filename for output

    # Constructor that builds the window
    def __init__(self):

        # Creates a window with title, set size
        self.root = Tk()
        self.root.title("Set Clock")
        self.root.minsize(950, 400)
        self.root.maxsize(950, 400)

        # Initialize the clock setting variables
        self._day = 0
        self._hour = 0
        self._minute = 0
        self._isAM = True
        self._exit = False
        self._mode = 0

        # Initialize and display time labels at top of window
        self.dayLabel = Label(self.root, font = ("helvetica", 14), padx= 20, pady = 20)
        self.dayLabel.grid(row = 0, column = 0)
        self.hourLabel = Label(self.root, font = ("helvetica", 14), pady = 20)
        self.hourLabel.grid(row = 0, column = 1)
        self.minuteLabel = Label(self.root, font = ("helvetica", 14), pady = 20)
        self.minuteLabel.grid(row = 0, column = 2)
        self.AMPM_Label = Label(self.root, font = ("helvetica", 14), pady = 20)
        self.AMPM_Label.grid(row = 0, column = 3)

        # Initialize the menu labels appearing on the left side of the window
        self.dayTextLabel = Label(self.root, text = "Set Day:", font = ("helvetica", 14), padx = 20, pady = 20)
        self.dayTextLabel.grid(row = 1, column = 0)
        self.hourTextLabel = Label(self.root, text = "Set Hour:", font = ("helvetica", 14), padx = 20, pady = 20)
        self.hourTextLabel.grid(row = 2, column = 0)
        self.minuteTextLabel = Label(self.root, text = "Set Minute:", font = ("helvetica", 14), padx = 20, pady = 20)
        self.minuteTextLabel.grid(row = 3, column = 0)
        self.AMPM_TextLabel = Label(self.root, text = "Set AM/PM:", font = ("helvetica", 14), padx = 20, pady = 20)
        self.AMPM_TextLabel.grid(row = 4, column = 0)
        self.exit_TextLabel = Label(self.root, text = "Exit", font = ("helvetica", 14), padx = 20, pady = 20)
        self.exit_TextLabel.grid(row = 5, column = 0)
        self.exitNo = Label(self.root, text = "No", font = ("helvetica", 10), padx = 20, pady = 20)
        self.exitNo.grid(row = 5, column = 1)
        self.exitYes = Label(self.root, text = "Yes", font = ("helvetica", 10), padx = 20, pady = 20)
        self.exitYes.grid(row = 5, column = 2)

        # List of weekday labels for the user to select from
        self.sunday = Label(self.root, text = "Sunday", font = ("helvetica", 10))
        self.sunday.grid(row = 1, column = 1)
        self.monday = Label(self.root, text = "Monday", font = ("helvetica", 10))
        self.monday.grid(row = 1, column = 3)
        self.tuesday = Label(self.root, text = "Tuesday", font = ("helvetica", 10))
        self.tuesday.grid(row = 1, column = 5)
        self.wednesday = Label(self.root, text = "Wednesday", font = ("helvetica", 10))
        self.wednesday.grid(row = 1, column = 7)
        self.thursday = Label(self.root, text = "Thursday", font = ("helvetica", 10))
        self.thursday.grid(row = 1, column = 9)
        self.friday = Label(self.root, text = "Friday", font = ("helvetica", 10))
        self.friday.grid(row = 1, column = 11)
        self.saturday = Label(self.root, text = "Saturday", font = ("helvetica", 10))
        self.saturday.grid(row = 1, column = 13)
        self._weekdays = [self.sunday, self.monday, self.tuesday, self.wednesday,
                        self.thursday, self.friday, self.saturday]
        # Highlight the currently selected weekday
        self._weekdays[self._day].config(bg = 'yellow')

        # List of hour labels for the user to select from
        self.hour_1 = Label(self.root, text = "1", font = ("helvetica", 10), padx = 20)
        self.hour_1.grid(row = 2, column = 1)
        self.hour_2 = Label(self.root, text = "2", font = ("helvetica", 10), padx = 20)
        self.hour_2.grid(row = 2, column = 2)
        self.hour_3 = Label(self.root, text = "3", font = ("helvetica", 10), padx = 20)
        self.hour_3.grid(row = 2, column = 3)
        self.hour_4 = Label(self.root, text = "4", font = ("helvetica", 10), padx = 20)
        self.hour_4.grid(row = 2, column = 4)
        self.hour_5 = Label(self.root, text = "5", font = ("helvetica", 10), padx = 20)
        self.hour_5.grid(row = 2, column = 5)
        self.hour_6 = Label(self.root, text = "6", font = ("helvetica", 10), padx = 20)
        self.hour_6.grid(row = 2, column = 6)
        self.hour_7 = Label(self.root, text = "7", font = ("helvetica", 10), padx = 20)
        self.hour_7.grid(row = 2, column = 7)
        self.hour_8 = Label(self.root, text = "8", font = ("helvetica", 10), padx = 20)
        self.hour_8.grid(row = 2, column = 8)
        self.hour_9 = Label(self.root, text = "9", font = ("helvetica", 10), padx = 20)
        self.hour_9.grid(row = 2, column = 9)
        self.hour_10 = Label(self.root, text = "10", font = ("helvetica", 10), padx = 20)
        self.hour_10.grid(row = 2, column = 10)
        self.hour_11 = Label(self.root, text = "11", font = ("helvetica", 10), padx = 20)
        self.hour_11.grid(row = 2, column = 11)
        self.hour_12 = Label(self.root, text = "12", font = ("helvetica", 10), padx = 20)
        self.hour_12.grid(row = 2, column = 12)
        self._hours = [self.hour_1, self.hour_2, self.hour_3, self.hour_4,
                    self.hour_5, self.hour_6, self.hour_7, self.hour_8,
                    self.hour_9, self.hour_10, self.hour_11, self.hour_12]
        # Highlight the currently selected hour
        self._hours[self._hour].config(bg = 'yellow')

        # List of minute labels for the user to select from, intervals of 5
        self.min_00 = Label(self.root, text = "00", font = ("helvetica", 10))
        self.min_00.grid(row = 3, column = 1)
        self.min_05 = Label(self.root, text = "05", font = ("helvetica", 10))
        self.min_05.grid(row = 3, column = 2)
        self.min_10 = Label(self.root, text = "10", font = ("helvetica", 10))
        self.min_10.grid(row = 3, column = 3)
        self.min_15 = Label(self.root, text = "15", font = ("helvetica", 10))
        self.min_15.grid(row = 3, column = 4)
        self.min_20 = Label(self.root, text = "20", font = ("helvetica", 10))
        self.min_20.grid(row = 3, column = 5)
        self.min_25 = Label(self.root, text = "25", font = ("helvetica", 10))
        self.min_25.grid(row = 3, column = 6)
        self.min_30 = Label(self.root, text = "30", font = ("helvetica", 10))
        self.min_30.grid(row = 3, column = 7)
        self.min_35 = Label(self.root, text = "35", font = ("helvetica", 10))
        self.min_35.grid(row = 3, column = 8)
        self.min_40 = Label(self.root, text = "40", font = ("helvetica", 10))
        self.min_40.grid(row = 3, column = 9)
        self.min_45 = Label(self.root, text = "45", font = ("helvetica", 10))
        self.min_45.grid(row = 3, column = 10)
        self.min_50 = Label(self.root, text = "50", font = ("helvetica", 10))
        self.min_50.grid(row = 3, column = 11)
        self.min_55 = Label(self.root, text = "55", font = ("helvetica", 10))
        self.min_55.grid(row = 3, column = 12)
        self._minutes = [self.min_00, self.min_05, self.min_10, self.min_15,
                        self.min_20, self.min_25, self.min_30, self.min_35,
                        self.min_40, self.min_45, self.min_50, self.min_55]
        # Highlight the currently selected minute
        self._minutes[self._minute].config(bg = 'yellow')

        # Label AM/PM for the user to select from
        self.am = Label(self.root, text = "A.M.", font = ("helvetica", 10))
        self.am.grid(row = 4, column = 1)
        self.pm = Label(self.root, text = "P.M.", font = ("helvetica", 10))
        self.pm.grid(row = 4, column = 2)

        # Highlight AM/PM, the one currently selected
        if (self._isAM):
            self.am.config(bg = 'yellow')
        else:
            self.pm.config(bg = 'yellow')
        self.dayTextLabel.config(bg = "yellow")

        self.exitNo.config(bg = "yellow")

        # Display the default time
        self.display_time()
        # Bind keys 'j', 'k', and spacebar
		# Help on this was from Hornof's sample code from Canvas
        self.root.bind('<j>', self.backward)
        self.root.bind('<l>', self.forward)
        self.root.bind('<k>', self.next_mode)

        # Display the window
        self.root.mainloop()


    ############################################################################
    # Updates all the labels at the top of the window to reflect the user's
    # currently set time.
    ############################################################################
    def display_time(self):

        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.dayLabel.config(text = (weekdays[self._day] + ", "))   # Display the weekday
        self.hourLabel.config(text = (str(self._hour + 1) + ":"))   # Display the hour
        self.minuteLabel.config(text = "{:02}".format(self._minute * 5))    # Display the minute
        if (self._isAM):
            self.AMPM_Label.config(text = " A.M.")  # Display 'A.M.'
        else:
            self.AMPM_Label.config(text = " P.M.")  # Display 'P.M.'

    ############################################################################
    # User scrolls forward, increment the currently selected value depending
    # on what mode the user is in (e.g. go from Thursday to Friday, 7 to 8, etc.)
    ############################################################################
    def forward(self, event):
        print("L")
        
        # User in set weekday state, increment the day
        if (self._mode == 0):
            self._weekdays[self._day].config(bg = 'gray95')
            self._day += 1
            # Ensure day does not exceed the maximum
            if (self._day > 6):
                self._day = 0
            # Plays the currently selected weekday
            self._weekdays[self._day].config(bg = 'yellow')
            self.play_current_weekday()
        
        # User in set hour state, increment the hour
        elif (self._mode == 1):
            self._hours[self._hour].config(bg = 'gray95')
            self._hour += 1
            # Ensure hour does not exceed the maximum
            if (self._hour > 11):
                self._hour = 0
            # Plays the currently selected hour
            self._hours[self._hour].config(bg = 'yellow')
            self.play_current_hour()

        # User in set minute state, increment the minute
        elif (self._mode == 2):
            self._minutes[self._minute].config(bg = 'gray95')
            self._minute += 1
            # Ensure minute does not exceed the maximum
            if (self._minute > 11):
                self._minute = 0
            # Plays the currently selected minute
            self._minutes[self._minute].config(bg = 'yellow')
            self.play_current_minute()

        # User in set AM PM state, switch the boolean
        elif (self._mode == 3):
            # Un-highlight both labels
            self.am.config(bg = 'gray95')
            self.pm.config(bg = 'gray95')
            self._isAM = not self._isAM
            # Highlight the correct label
            if (self._isAM):
                self.am.config(bg = 'yellow')
            else:
                self.pm.config(bg = 'yellow')
            # Play 'AM' or 'PM' depending which is currently selected
            self.play_AM_PM()
        elif (self._mode == 4):
            # Un-highlight both labels
            self.exitNo.config(bg = 'gray95')
            self.exitYes.config(bg = 'gray95')
            self._exit = not self._exit
            # Highlight the correct label
            if (self._exit):
                self.exitYes.config(bg = 'yellow')
            else:
                self.exitNo.config(bg = 'yellow')

    ############################################################################
    # User scrolls backwards, decrement the currently selected value depending
    # on what mode the user is in (e.g. go from Monday to Sunday, 3 to 2, etc.)
    ############################################################################
    def backward(self, event):
        print("J")
        
        # User in set weekday state, decrement the day
        if (self._mode == 0):
            self._weekdays[self._day].config(bg = 'gray95')
            self._day -= 1
            # Ensure day does not go beneath the minimum
            if (self._day < 0):
                self._day = 6
            # Plays the currently selected weekday
            self._weekdays[self._day].config(bg = 'yellow')
            self.play_current_weekday()
        
        # User in set hour state, decrement the hour
        elif (self._mode == 1):
            self._hours[self._hour].config(bg = 'gray95')
            self._hour -= 1
            # Ensure hour does not go beneath the minimum
            if (self._hour < 0):
                self._hour = 11
            # Plays the currently selected hour
            self._hours[self._hour].config(bg = 'yellow')
            self.play_current_hour()

        # User in set minute state, decrement the minute
        elif (self._mode == 2):
            self._minutes[self._minute].config(bg = 'gray95')
            self._minute -= 1
            # Ensure minute does not go beneath the minimum
            if (self._minute < 0):
                self._minute = 11
            # Plays the currently selected minute
            self._minutes[self._minute].config(bg = 'yellow')
            self.play_current_minute()

        # User in set AM PM state, switch the boolean
        elif (self._mode == 3):
            # Un-highlight both labels
            self.am.config(bg = 'gray95')
            self.pm.config(bg = 'gray95')
            self._isAM = not self._isAM
            # Highlight the correct label
            if (self._isAM):
                self.am.config(bg = 'yellow')
            else:
                self.pm.config(bg = 'yellow')
            # Play 'AM' or 'PM' depending which is currently selected
            self.play_AM_PM()
        elif (self._mode == 4):
            # Un-highlight both labels
            self.exitNo.config(bg = 'gray95')
            self.exitYes.config(bg = 'gray95')
            self._exit = not self._exit
            # Highlight the correct label
            if (self._exit):
                self.exitYes.config(bg = 'yellow')
            else:
                self.exitNo.config(bg = 'yellow')

    ############################################################################
    # Transition to the next mode. Highlight & gray out the appropriate labels.
    ############################################################################
    def next_mode(self, event):
        print("K")
        
        if (self._mode == 4 and self._exit):
            self.root.quit()

        # Gray out all sections
        self.dayTextLabel.config(bg = "gray95")
        self.hourTextLabel.config(bg = "gray95")
        self.minuteTextLabel.config(bg = "gray95")
        self.AMPM_TextLabel.config(bg = "gray95")
        self.exit_TextLabel.config(bg = "gray95")
        # Increment the mode, ensure it does not exceed maximum
        self._mode += 1
        if (self._mode > 5):
            self._mode = 0

        # User in weekday mode
        if (self._mode == 0):
            print("SET WEEKDAY ***")
            sound.Play(self.SET_WEEKDAY_WAV)
            self.dayTextLabel.config(bg = "yellow")
        # User in hour mode
        elif (self._mode == 1):
            print("SET HOUR ***")
            sound.Play(self.SET_HOUR_WAV)
            self.hourTextLabel.config(bg = "yellow")
        # User in minute mode
        elif (self._mode == 2):
            print("SET MINUTE ***")
            sound.Play(self.SET_MINUTE)
            self.minuteTextLabel.config(bg = "yellow")
        # User in AM/PM mode
        elif (self._mode == 3):
            print("SET AM/PM ***")
            #sound.Play(self.SET_AM_PM)
            self.AMPM_TextLabel.config(bg = "yellow")
        elif (self._mode == 4):
            print("EXIT ***")
            self.exit_TextLabel.config(bg = "yellow")
        # User in time report mode
        else:
            text = "AM"
            if (not self._isAM):
                text = "PM"
            weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            print(weekdays[self._day] + ",", str(self._hour + 1) + ":" + \
                str("{:02}".format(self._minute * 5)), text)
            self.display_time()
            self.play_complete_time()


    ################################################################################
    # Plays the currently selected weekday to the user. Simply accesses the global
    # list storing the weekdays, where index 0 is Sunday, 1 is Monday, etc.
    ################################################################################
    def play_current_weekday(self):
        if (self._day >= 0 and self._day <= 6):
            sound.Play(self.WEEKDAYS_WAV[self._day])

    ################################################################################
    # Plays the currently selected hour to the user. The function accesses the time
    # directory where all the numbered .wav files are stored. The hour is then
    # simply converted into a string, concatenated onto the directory, followed
    # by '.wav', and the sound file is played.
    ################################################################################
    def play_current_hour(self):
        if (self._hour >= 0 and self._hour <= 11):
            sound.Play(self.TIME_WAV_DIR + str("{:02}".format(self._hour + 1)) + "_f.wav")

    ################################################################################
    # Plays the currently selected minute to the user. The function uses the
    # numbered .wav files in the /time/ directory. If the minute is less than ten,
    # the number is preceded by 'oh' (e.g. if minute is 1, play 'oh one'). If the
    # number is 0, 'oh oh' is played. Otherwise, the corresponding numbered .wav
    # file is played (e.g. if minute is 34, play 34.wav).
    ################################################################################
    def play_current_minute(self):
        # Minute selected is zero, play 'oh oh'
        if (self._minute == 0):
            sound.combine_wav_files(self.TMP_FILE_WAV, self.OH_WAV, self.OH_WAV)
            sound.Play(self.TMP_FILE_WAV)
        # Minute selected is 1-9, play 'oh' followed by the minute
        elif ((self._minute * 5) <= 9):
            sound.combine_wav_files(self.TMP_FILE_WAV, self.OH_WAV, self.TIME_WAV_DIR + \
                str("{:02}".format(self._minute * 5)) + "_f.wav")
            sound.Play(self.TMP_FILE_WAV)
        # Minute selected is 11-59, simply play corresponding file
        else:
            sound.Play(self.TIME_WAV_DIR + str(self._minute * 5) + "_f.wav")

    ################################################################################
    # Plays 'AM' or 'PM' to the user given the parameter is_AM. if is_AM is true,
    # the program plays 'am.wav', or 'pm.wav' if otherwise.
    ################################################################################
    def play_AM_PM(self):
        if self._isAM:
            sound.Play(self.AM_WAV)  # Play 'AM'
        else:
            sound.Play(self.PM_WAV)  # Play 'PM'

    ################################################################################
    # Plays the complete time to the user given the weekday, hour, minute, and
    # AM/PM.
    ################################################################################
    def play_complete_time(self):
        # Checks which am/pm file to play; assigns to 'am.wav' or 'pm.wav'
        am_pm_wav = self.PM_WAV
        if self._isAM:
            am_pm_wav = self.AM_WAV
        # If the minute is 0, play the hour followed by 'o clock'
        # For example: 'Thursday, 12 o clock PM'
        if (self._minute == 0):
            sound.combine_wav_files(self.TMP_FILE_WAV, self.YOU_SELECTED_WAV, self.WEEKDAYS_WAV[self._day],\
                                    self.TIME_WAV_DIR + str("{:02}".format(self._hour + 1)) + "_f.wav", self.OH_CLOCK_WAV, am_pm_wav)
        # Else if the minute is 1-9, play 'oh' before the minute
        # For example: 'Thursday, 12 oh 5 PM'
        elif ((self._minute * 5) <= 9):
            sound.combine_wav_files(self.TMP_FILE_WAV, self.YOU_SELECTED_WAV, self.WEEKDAYS_WAV[self._day],\
                                    self.TIME_WAV_DIR + str("{:02}".format(self._hour + 1)) + "_f.wav", self.OH_WAV,\
                                    self.TIME_WAV_DIR + str("{:02}".format(self._minute * 5)) + "_f.wav", am_pm_wav)
        # Otherwise, play the corresponding numbered file (e.g. 34 plays '34.wav')
        else:
            sound.combine_wav_files(self.TMP_FILE_WAV, self.YOU_SELECTED_WAV, self.WEEKDAYS_WAV[self._day],\
                                    self.TIME_WAV_DIR + str("{:02}".format(self._hour + 1)) + "_f.wav", self.TIME_WAV_DIR + \
                                    str("{:02}".format(self._minute * 5)) + "_f.wav", am_pm_wav)
        sound.Play(self.TMP_FILE_WAV)    # Play the complete time file



#########################################################
# Create & display the window
print("set_clock_2")
window = ClockWindow()
#########################################################
