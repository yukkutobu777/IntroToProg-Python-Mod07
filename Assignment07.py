# ------------------------------------------------- #
# Title: Assginment 07
# Description: Steps to build a shed saved to binary file
# ChangeLog: (Who, When, What)
# KBosworth,11/17/2020,Created Script
# KBosworth,11/17/2020,Finished Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!
import sys  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'Steps.dat'
lstSteps = []

# Processing -------------------------------------- #
class CustomError(Exception):
    def __str__(self):
        """"This is a custom error when when the user does not want to proceed and exit the program"""
        return "The program will exit now."

class FileHandling:
    def does_file_exist(file_name):
        """
        Desc - Checks to see if a file exists
        :param file_name: (file) file to be checked:
        :return: nothing
        """
        try:
            objFile = open(file_name, "rb")
            objFile.close()
        except FileNotFoundError:
            #print("File does not exist.")
            choice = input("File does not exist. Create one? y/n \n")
            try:
                if choice.lower() == 'y':
                    objFile = open(file_name, "wb+")
                    objFile.close()
                else:
                    raise CustomError()
            except Exception as e:
                print(e, e.__doc__, type(e), sep='\n')
                sys.exit(1)

    def save_data_to_file(file_name, list_of_data):
        """
        Desc - Saves an item input by the user into the table
        :param file_name: (file) file to be written to:
        :param list_of_data: (list) data to be written to file:
        :return: nothing
        """
        objFile=open(file_name, "ab")
        pickle.dump(list_of_data, objFile)
        objFile.close()

    def read_data_from_file(file_name):
        """
        Desc - Removes an item input by the user into the table
        :param file_name: (file) file that will be read
        :return: list
        """
        list_of_data = []
        with (open(file_name, "rb")) as objFile:
            while True:
                try:
                    list_of_data.append(pickle.load(objFile))
                except EOFError:
                    break
        objFile.close()
        for row in list_of_data:
            print(row[0] + " (" + row[1] + ")")
        print()

# Presentation ------------------------------------ #
# TODO: check to see if the file exists
FileHandling.does_file_exist(strFileName)

# TODO: read the contents of the binary file
print("These are the steps documented to build the shed:")
FileHandling.read_data_from_file(strFileName)

# TODO: ask for input
step = input("Enter a step: ")
phase = input("Enter a phase (plan, prep, build, finish: ")
lstSteps=[step, phase]

# TODO: store the list object into a binary file
FileHandling.save_data_to_file(strFileName,lstSteps)

# # TODO: read the data from the file after updates have been saved
print("Here is the list after your additions:")
FileHandling.read_data_from_file(strFileName)