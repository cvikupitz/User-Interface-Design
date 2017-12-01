################################################################################
# set_clock.py
# Author - Cole Vikupitz, Oct 2017
# CIS 443 Project 1
#
# A time application that allows the user to set the day of the week and current
# time, and have the application report the full time back; this is all done
# using auditory commands and single keystrokes. The application has a number
# of states that the user must navigate through to set and hear the set day and
# time.
#
################################################################################

# Package imports
import readchar     # for readchar.readchar()
import time         # for time.sleep()

# Local imports
import sound        # sound.py accompanies this file

################################################################################
# main()
################################################################################
def main():
    create_sound_filenames()
    verify_sound_filenames()    # Comment out if start-up to slow
    create_menu_globals()
    run_menu()

################################################################################
# Create the sound objects for the auditory menus and display.
################################################################################
def create_sound_filenames():

    # Declare global variables
    global INTRO_WAV, HELP_WAV, PRESS_FOR_HELP, PRESS_TO_QUIT, PRESS_AGAIN_TO_QUIT_WAV,\
        YOU_SELECTED_WAV, SET_WEEKDAY_WAV, SET_HOUR_WAV, SET_MINUTE, SET_AM_PM, WEEKDAYS_WAV,\
        TIME_WAV_DIR, OH_WAV, AM_WAV, PM_WAV, OH_CLOCK_WAV, EXITING_PROGRAM_WAV,\
        EXITING_PROGRAM_WAV_DURATION, TMP_FILE_WAV

    # Sounds for the introduction message, help messages, etc.
    misc_path = "program_wav_files/miscellaneous/"
    INTRO_WAV = misc_path + "intro.wav"
    HELP_WAV = misc_path + "help_message.wav"
    PRESS_FOR_HELP = misc_path + "press_l_for_help.wav"
    PRESS_TO_QUIT = misc_path + "press_sc_to_quit.wav"
    PRESS_AGAIN_TO_QUIT_WAV = misc_path + "press_again_to_quit.wav"
    YOU_SELECTED_WAV = misc_path + "you_selected.wav"
    # Sounds for announcing the system's current state; set the weekday, hour, minute, etc.
    SET_WEEKDAY_WAV = misc_path + "set_weekday.wav"
    SET_HOUR_WAV = misc_path + "set_hour.wav"
    SET_MINUTE = misc_path + "set_minute.wav"
    SET_AM_PM = misc_path + "set_am_pm.wav"

    # Keep a list of sounds used for the weekdays for easier use
    # Indexed access: 0 for Sunday, 1 for Monday, ..., 5 for Friday, 6 for Saturday
    weekday_path = "program_wav_files/weekdays/"
    WEEKDAYS_WAV = [weekday_path + "sunday.wav",
                    weekday_path + "monday.wav",
                    weekday_path + "tuesday.wav",
                    weekday_path + "wednesday.wav",
                    weekday_path + "thursday.wav",
                    weekday_path + "friday.wav",
                    weekday_path + "saturday.wav"]

    # Keep global for time directory for simpler access to sound files
    TIME_WAV_DIR = "program_wav_files/time/"
    # Sound files for AM, PM, O 'clock, etc.
    OH_WAV = TIME_WAV_DIR + "0.wav"
    AM_WAV = TIME_WAV_DIR + "am.wav"
    PM_WAV = TIME_WAV_DIR + "pm.wav"
    OH_CLOCK_WAV = TIME_WAV_DIR + "o_clock.wav"

    # Any other sound file(s) the program may need
    EXITING_PROGRAM_WAV = misc_path + "exiting.wav"
    EXITING_PROGRAM_WAV_DURATION = 1.3  # Duration to sleep() for exiting message

    TMP_FILE_WAV = "tmp_file_p782s8u.wav" # Random filename for output    


################################################################################
# Verify all files can be loaded and played.
# Play all sound files to make sure the paths and filenames are correct and valid.
# The very last sound tested/played should be the sound that plays at startup.
################################################################################
def verify_sound_filenames():
    print("Verifying sound files...")
    sound.Play(HELP_WAV)
    sound.Play(PRESS_FOR_HELP)
    sound.Play(PRESS_TO_QUIT)
    sound.Play(PRESS_AGAIN_TO_QUIT_WAV)
    sound.Play(YOU_SELECTED_WAV)
    sound.Play(SET_WEEKDAY_WAV)
    sound.Play(SET_HOUR_WAV)
    sound.Play(SET_MINUTE)
    sound.Play(SET_AM_PM)
    for day in WEEKDAYS_WAV:
        sound.Play(day)
    for i in range(60):
        sound.Play(TIME_WAV_DIR + str(i) + ".wav")
    sound.Play(OH_WAV)
    sound.Play(AM_WAV)
    sound.Play(PM_WAV)
    sound.Play(OH_CLOCK_WAV)
    sound.Play(EXITING_PROGRAM_WAV)
    sound.Play(INTRO_WAV)

################################################################################
# Create some global constants and variables for the menu.
################################################################################
def create_menu_globals():

    # Declare global variables as such.
    global SELECT_KEY, BACKWARD_KEY, FORWARD_KEY, HELP_KEY, QUIT_KEY, MINIMAL_HELP_STRING

    # Constants
    # Keystrokes for the keyboard interaction.
    SELECT_KEY = '\x20'     # space bar
    BACKWARD_KEY = 'j'
    FORWARD_KEY = 'k'
    HELP_KEY = 'l'
    QUIT_KEY = ';'
    
    # A bare minimum of text to display to guide the user.
    MINIMAL_HELP_STRING = "Press '" + HELP_KEY + "' for help. Press '" + QUIT_KEY + "' to quit."

################################################################################
# Announces the program's current state auditorily to the user, given the state
# parameter. For example, if the state is 1, play 'Set hour' to the user.
################################################################################
def play_current_state(state):
    if (state == 0):
        # Announce state for setting the day of the week
        sound.Play(SET_WEEKDAY_WAV)
    elif (state == 1):
        # Announce state for setting the hour
        sound.Play(SET_HOUR_WAV)
    elif (state == 2):
        # Announce state for setting the minute
        sound.Play(SET_MINUTE)
    elif (state == 3):
        # Announce state for setting AM or PM
         sound.Play(SET_AM_PM)
    # Ignore any other state passed in

################################################################################
# Plays the currently selected weekday to the user. Simply accesses the global
# list storing the weekdays, where index 0 is Sunday, 1 is Monday, etc.
################################################################################
def play_current_weekday(day):
    if (day >= 0 and day <= 6):
        sound.Play(WEEKDAYS_WAV[day])

################################################################################
# Plays the currently selected hour to the user. The function accesses the time
# directory where all the numbered .wav files are stored. The hour is then
# simply converted into a string, concatenated onto the directory, followed
# by '.wav', and the sound file is played.
################################################################################
def play_current_hour(hour):
    if (hour >= 1 and hour <= 12):
        sound.Play(TIME_WAV_DIR + str(hour) + ".wav")

################################################################################
# Plays the currently selected minute to the user. The function uses the
# numbered .wav files in the /time/ directory. If the minute is less than ten,
# the number is preceded by 'oh' (e.g. if minute is 1, play 'oh one'). If the
# number is 0, 'oh oh' is played. Otherwise, the corresponding numbered .wav
# file is played (e.g. if minute is 34, play 34.wav).
################################################################################
def play_current_minute(minute):
    # Minute selected is zero, play 'oh oh'
    if (minute == 0):
        sound.combine_wav_files(TMP_FILE_WAV, OH_WAV, OH_WAV)
        sound.Play(TMP_FILE_WAV)
    # Minute selected is 1-9, play 'oh' followed by the minute
    elif (minute >= 1 and minute <= 9):
        sound.combine_wav_files(TMP_FILE_WAV, OH_WAV, TIME_WAV_DIR + str(minute) + ".wav")
        sound.Play(TMP_FILE_WAV)
    # Minute selected is 11-59, simply play corresponding file
    elif (minute >= 10 and minute <= 59):
        sound.Play(TIME_WAV_DIR + str(minute) + ".wav")

################################################################################
# Plays 'AM' or 'PM' to the user given the parameter is_AM. if is_AM is true,
# the program plays 'am.wav', or 'pm.wav' if otherwise.
################################################################################
def play_AM_PM(is_AM):
    if is_AM:
        sound.Play(AM_WAV)  # Play 'AM'
    else:
        sound.Play(PM_WAV)  # Play 'PM'

################################################################################
# Plays the help message to the user, preceded by which mode they are in.
# Invoked when the user presses the help button, in any state.
################################################################################
def play_help(state):
    if (state == 0):
        # User in weekday state, precede help message with 'Set day of week'
        sound.combine_wav_files(TMP_FILE_WAV, SET_WEEKDAY_WAV, HELP_WAV)
    elif (state == 1):
        # User in hour state, precede help message with 'Set hour'
        sound.combine_wav_files(TMP_FILE_WAV, SET_HOUR_WAV, HELP_WAV)
    elif (state == 2):
        # User in minute state, precede help message with 'Set minute'
        sound.combine_wav_files(TMP_FILE_WAV, SET_MINUTE, HELP_WAV)
    elif (state == 3):
        # User in AM/PM state, plays 'Set AM PM'
        sound.combine_wav_files(TMP_FILE_WAV, SET_AM_PM, HELP_WAV)
    else:
        # Otherwise, just play help message by itself
        sound.combine_wav_files(TMP_FILE_WAV, HELP_WAV)
    sound.Play(TMP_FILE_WAV)    # Play full help message

################################################################################
# Plays the complete time to the user given the weekday, hour, minute, and
# AM/PM.
################################################################################
def play_complete_time(day, hour, minute, is_AM):
    # Checks which am/pm file to play; assigns to 'am.wav' or 'pm.wav'
    am_pm_wav = PM_WAV
    if is_AM:
        am_pm_wav = AM_WAV
    # If the minute is 0, play the hour followed by 'o clock'
    # For example: 'Thursday, 12 o clock PM'
    if (minute == 0):
        sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV, WEEKDAYS_WAV[day],\
                                TIME_WAV_DIR + str(hour) + ".wav", OH_CLOCK_WAV, am_pm_wav)
    # Else if the minute is 1-9, play 'oh' before the minute
    # For example: 'Thursday, 12 oh 5 PM'
    elif (minute >= 1 and minute <= 9):
        sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV, WEEKDAYS_WAV[day],\
                                TIME_WAV_DIR + str(hour) + ".wav", OH_WAV,\
                                TIME_WAV_DIR + str(minute) + ".wav", am_pm_wav)
    # Otherwise, play the corresponding numbered file (e.g. 34 plays '34.wav')
    else:
        sound.combine_wav_files(TMP_FILE_WAV, YOU_SELECTED_WAV, WEEKDAYS_WAV[day],\
                                TIME_WAV_DIR + str(hour) + ".wav", TIME_WAV_DIR + str(minute) + ".wav",\
                                am_pm_wav)
    sound.Play(TMP_FILE_WAV)    # Play the complete time file

################################################################################
# Run the menu in an endless loop until the user exits.
################################################################################
def run_menu():

    # Initialize time variables and current system state
    day = 0
    hour = 12
    minute = 0
    is_AM = True
    state = 4

    # Print the minimal help string and play the introductory file
    print(MINIMAL_HELP_STRING)
    sound.Play(INTRO_WAV)
    # Get the first keystroke.
    c = readchar.readchar()

    # Endless loop responding to the user's last keystroke.
    # The loop breaks when the user hits the QUIT_KEY.
    while True:

        # User presses the forward key
        if c == FORWARD_KEY:
            # User in set weekday state, increment the day
            if  (state == 0):
                day += 1
                # Ensure day does not exceed the maximum
                if (day > 6):
                    day = 0
                # Plays the currently selected weekday
                play_current_weekday(day)
            # User in set hour state, increment the hour
            elif (state == 1):
                hour += 1
                # Ensure hour does not exceed the maximum
                if (hour > 12):
                    hour = 1
                play_current_hour(hour)
            # User in set minute state, increment the minute
            elif (state == 2):
                minute += 1
                # Ensure day does not exceed the maximum
                if (minute > 59):
                    minute = 0
                play_current_minute(minute)
            # User in set AM PM state, switch the boolean
            elif (state == 3):
                is_AM = not is_AM
                # Play 'AM' or 'PM' depending which is currently selected
                play_AM_PM(is_AM)
            # User in timer mode, play the full current time
            elif (state == 4):
                play_complete_time(day, hour, minute, is_AM)
                
        # User presses the backwards key
        if c == BACKWARD_KEY:
            # User in set weekday state, decrement the day
            if (state == 0):
                day -= 1
                # Ensure day does not go below 0
                if (day < 0):
                    day = 6
                play_current_weekday(day)
            # User in set hour state, decrement the hour
            elif (state == 1):
                hour -= 1
                # Ensure hour does not go below 0
                if (hour < 1):
                    hour = 12
                play_current_hour(hour)
            # User in set minute state, decrement the minute
            elif (state == 2):
                minute -= 1
                # Ensure minute does not go below 0
                if (minute < 0):
                    minute = 59
                play_current_minute(minute)
            # User in set AM PM state, switch the boolean
            elif (state == 3):
                is_AM = not is_AM
                # Play 'AM' or 'PM' depending which is currently selected
                play_AM_PM(is_AM)
             # User in timer mode, play the full current time
            elif (state == 4):
                play_complete_time(day, hour, minute, is_AM)

        # User presses the help key
        if c == HELP_KEY:
            play_help(state)
                
        # User presses the select key, go to next state
        if c == SELECT_KEY:
            state += 1
            # If user in timer mode, play the current full time
            if (state == 4):
                play_complete_time(day, hour, minute, is_AM)
            # Reset state back to 0 if after last state
            if (state > 4):
                state = 0
            # Announce the current state to the user
            play_current_state(state)

        # User quits.
        if c == QUIT_KEY:

            # Notify the user that another QUIT_KEY will quit the program.
            sound.Play(PRESS_AGAIN_TO_QUIT_WAV)

            # Get the user's next keystroke.
            c = readchar.readchar()

            # If the user pressed QUIT_KEY, quit the program.
            if c == QUIT_KEY:
                sound.Play(EXITING_PROGRAM_WAV)
                # A delay is needed so the sound gets played before quitting.
                time.sleep(EXITING_PROGRAM_WAV_DURATION)
                sound.cleanup()
                # Quit the program.
                break

        # The user presses a key that will have no effect.
        else:
            # Get the user's next keystroke.
            c = readchar.readchar()

################################################################################
main()
################################################################################
