import io

from Utils.Logger import logger

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""""")

    try:
        file = open(filepath)
    except:
        pass