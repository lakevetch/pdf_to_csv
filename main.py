import tabula
import os

DIR = os.listdir(os.curdir)

def main():

    welcome()

    while True:
        in_file = choose_pdf()

        out_file = convert_to_csv(in_file)

        cont = confirmation(out_file)
        if not cont == "y":
            break
        print()

def welcome():
    print("Welcome to the pdf to csv table converter!"
          "\nThis app will extract a table from a pdf and export it as a csv"
          " file.")
    print("\nYou will need to place the file you wish to convert into the"
          " folder where this \napp's main.py file lives. If you do not see"
          " your file, please quit and add it \nto the folder before"
          " returning.")
    print("\nIf you do not have Java installed on your computer, please quit"
          " and install it \nbefore returning.\n")

def choose_pdf():
    i = 1
    print("Files in current directory: ")
    for file in DIR:
        print(str(i) + ": " + file)
        i += 1
    print()
    index = validate_int("Enter the number of the file to convert: ")
    index -= 1
    return index

def convert_to_csv(index):
    out_file = validate_csv('Enter desired output filename with .csv extension'
                     ' (e.g. "file.csv"): ')
    tabula.convert_into(DIR[index], out_file, output_format="csv", pages="all")
    return out_file

def confirmation(out_file):
    if out_file in DIR:
        print("Success!")
    else:
        print("Something went wrong, contact Jack to troubleshoot.")
    cont = validate_y_n("Convert another? (y/n): ")
    return cont

def validate_int(prompt="Enter integer: "):
    message = "Please enter a positive non-zero integer within the range of" \
              " numbers listed."
    while True:
        try:
            integer = int(input(prompt))
            if integer > 0 and integer < len(DIR) + 1:
                return integer
            else:
                print(message)
        except:
            print(message)

def validate_y_n(prompt="Enter y/n: "):
    message = 'Please enter either a "y" or "n".'
    while True:
        answer = input(prompt)
        answer = answer.strip()
        answer = answer[0].lower()
        if not answer == "y" and not answer == "n":
            print(message)
        else:
            return answer

def validate_csv(prompt="Enter .csv filename: "):
    message = 'Already a file with that name.'
    while True:
        filename = input(prompt)
        if filename in DIR:
            print(message)
            overwrite = validate_y_n("Overwrite file? (y/n): ")
            if overwrite == "y":
                return filename
        else:
            return filename

main()