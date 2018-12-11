import sys
import time

# ------------------------------------------------------------------------
# Class Name: Logger
# Description  : Allows for logging of stdout to a text file.
# ------------------------------------------------------------------------


class Logger(object):

    # ------------------------------------------------------------------------
    # Function Name: __init__(self)
    # Arguments    :
    #  - descriptor: Descriptive string used in the filename i.e. LEMR20XX
    #                DEPLOYMENT TEST AMBIENT
    # Description  : Sets the terminal to sys.stdout and opens a log file with
    #                the current date and time as the filename.
    # Return Values: N/A
    # ------------------------------------------------------------------------

    def __init__(self, descriptor):
        self.terminal = sys.stdout
        filename = str(descriptor) + ' ' + str(time.ctime()) + '.txt'
        self.log = open(filename, 'w')

    # ------------------------------------------------------------------------
    # Function Name: write(self, message)
    # Arguments    :
    #   - message  : Message to write to the terminal and log file
    # Description  : Writes the provided message to the terminal and log file.
    # Return Values: N/A
    # ------------------------------------------------------------------------

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
