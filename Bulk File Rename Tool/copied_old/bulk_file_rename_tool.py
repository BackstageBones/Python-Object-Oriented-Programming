import os
import shutil
import filetype


class FileRenameTool(object):
    def __init__(self):
        self._os = os
        self._shutil = shutil
        self._filetype = filetype

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

    def rename_files_in_folder(self, ):
        images_extensions = ('.jpg', '.png', '.psd', '.tiff',)
        documents_extensions = ('.doc', '.txt', '.pdf')
        # ask which files would you like to rename
        user_specify = input(
            "Which files would you like to rename? \n type 'images' for images or 'text for text files")
        if user_specify in ('images', 'pictures'):
            user_naming = input("Provide file naming convention")
            i = 0
            for file in self._os.listdir(self._os.getcwd()):
                i += 1
                if self._os.path.isfile(file):
                # name, ext = self._os.path.splitext(file)
                    kind = self._filetype.guess(self._os.path.abspath(file))
                    if kind:
                        print(kind)

    """        
     elif user_specify in ('text', 'documents'):
         user_input = input("Provide file naming convention")
         i = 0
         for file in self._os.listdir(self._os.getcwd()):
             i += 1
             name, ext = self._os.path.splitext(file)
             if ext == documents_extensions[0]:
                 self._os.rename(file, user_input + '_' + str(i) + documents_extensions[0])
             elif ext == documents_extensions[1]:
                 self._os.rename(file, user_input + '_' + str(i) + documents_extensions[1])
             elif ext == documents_extensions[2]:
                 self._os.rename(file, user_input + '_' + str(i) + documents_extensions[2])
             else:
                 break
     else:
         return "unknown file type, cannot rename"
 """

    def make_copy(self):
        copy_place = self._os.getcwd() + "//copied_old"
        try:
            self._os.mkdir(copy_place)
        except OSError:
            print("Folder cannot be created")
        else:
            for file_name in self._os.listdir(self._os.getcwd()):
                full_file_name = self._os.path.join(self._os.getcwd(), file_name)
                if self._os.path.isfile(full_file_name):
                    try:
                        self._shutil.copy(file_name, copy_place)
                    except shutil.SameFileError:
                        print("Source and destination represents the same file.")
                    except PermissionError:
                        print("Permission denied.")
        finally:
            print("Copy made")


if __name__ == "__main__":
    BulkTool = FileRenameTool()
    BulkTool.change_directory()
    BulkTool.make_copy()
    BulkTool.rename_files_in_folder()
