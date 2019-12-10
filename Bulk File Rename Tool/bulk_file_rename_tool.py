import os
import shutil
import functools
import filetype


class FileRenameTool(object):
    def __init__(self):
        self._os = os
        self._shutil = shutil
        self._filetype = filetype

    class __CopyMakerDecorator(object):
        def __init__(self, decorated):
            self.decorated = decorated

        def __get__(self, obj, objtype):
            """Support instance methods."""
            return functools.partial(self.__call__, obj)

        def __call__(self, obj, *args, **kwargs):
            ask_for_copy = input("Would you like to make a copy of your files before renaming ?")
            if ask_for_copy in ('y', 'yes'):
                return self.decorated(obj, *args, **kwargs)

    class __ChangeDirectoryDecorator(object):
        def __init__(self, decorated):
            self.decorated = decorated

        def __get__(self, obj, objtype):
            """Support instance methods."""
            return functools.partial(self.__call__, obj)

        def __call__(self, obj, *args, **kwargs):
            ask_to_change_dir = input("Would you like to change directory ?")
            if ask_to_change_dir in ('y', 'yes'):
                return self.decorated(obj, *args, **kwargs)

    def __str__(self):
        return "Your current working directory is: \n {} and it contains these files \n {}".format(self._os.getcwd(),
                                                                                                   self._os.listdir(
                                                                                                       self._os.getcwd()))

    @__ChangeDirectoryDecorator
    def _change_directory(self):
        user_directory = input("Provide a path to navigate to: ")
        try:
            # Change the current working Directory
            self._os.chdir(user_directory)
            print("Directory changed")
        except OSError:
            print("Can't change the Current Working Directory")
        finally:
            print(self._os.listdir(self._os.getcwd()))

    def _rename_files_in_folder(self):
        images_extensions = ('jpg', 'png', 'psd', 'tiff',)
        documents_extensions = ('.doc', '.txt', '.pdf')
        # ask which files would you like to rename
        user_specify = input(
            "Which files would you like to rename? \n type 'images' for images or 'text' for text files ")
        if user_specify in ('images', 'pictures'):
            user_naming = input("Provide file naming convention")
            i = 0
            for file in self._os.listdir(self._os.getcwd()):
                i += 1
                if self._os.path.isfile(file):
                    kind = self._filetype.guess(self._os.path.abspath(file))
                    if kind is not None:
                        if kind.extension in images_extensions:
                            self._os.rename(file, user_naming + '_' + str(i) + '.' + str(kind.extension))

        elif user_specify in ('text', 'documents'):
            user_naming = input("Provide file naming convention")
            i = 0

            for file in self._os.listdir(self._os.getcwd()):
                i += 1
                if self._os.path.isfile(file):
                    kind = self._filetype.guess(self._os.path.abspath(file))
                    if kind is not None:
                        if kind.extension in documents_extensions:
                            self._os.rename(file, user_naming + '_' + str(i) + '.' + str(kind.extension))
        else:
            return "unknown file type, cannot rename"

    @__CopyMakerDecorator
    def _make_copy(self):
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
    BulkTool.__str__()
    BulkTool._change_directory()
    BulkTool._make_copy()
    BulkTool._rename_files_in_folder()
