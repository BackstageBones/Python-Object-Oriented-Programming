import os
import shutil


class FileRenameTool(object):
    def __init__(self):
        self._os = os
        self._shutil = shutil

    def _print_current_directory(self):
        print("Your current working directory is: \n {}".format(self._os.getcwd()))
        print("The folder contains these files: ", self._os.listdir(self._os.getcwd()))

    def change_directory(self):
        user_directory = input("Provide a path to navigate to: ")
        try:
            # Change the current working Directory
            self._os.chdir(user_directory)
            print("Directory changed")
        except OSError:
            print("Can't change the Current Working Directory")
        finally:
            print(self._os.listdir(self._os.getcwd()))


    def rename_files_in_folder(self,):

        user_input = input("Provide file naming convention")
        for file in self._os.listdir(self._os.getcwd()):
            for i in range(len(self._os.listdir(self._os.getcwd()))):
                self._os.rename(file, user_input + '_' + str(i))

    def make_copy(self,):
        try:
            self._os.mkdir(self._os.getcwd()+"copied_old")
        except OSError:
            print("Folder cannot be created")

        for file in self._os.listdir(self._os.getcwd()):
            try:
                self._shutil.copy(self._os.getcwd(), "copied_old")
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
            except PermissionError:
                print("Permission denied.")






if __name__ == "__main__":
    BulkTool = FileRenameTool()
    BulkTool.change_directory()
    BulkTool.make_copy()
    BulkTool._print_current_directory()
    BulkTool.rename_files_in_folder()

