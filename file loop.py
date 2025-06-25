import os


def get_folder_path():
    """
    this function is used to get the folder path
    :return: a folder path
    """
    folder_path = input("Enter the folder path: ")
    return folder_path

def get_file_path():
    """
    this function is used to get the file path
    :return: the file path
    """
    folder_path = get_folder_path()
    print("Enter the file name: ")
    file_name = input()
    return os.path.join(folder_path, file_name)


def open_file():
    """
    this function is used to open the file
    :return: the opened file content
    """
    file_path = get_file_path()
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            print(file_content)
            file.close()
    except FileNotFoundError:
        print("The file doesn't exist: FileNotFoundError")
    return open_file()


def main():
    open_file()


if __name__ == "__main__":
    main()
