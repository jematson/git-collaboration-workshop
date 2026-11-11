# TODO: Write a program that prints a box


def main():
    while True:
        try:
            width = int(input("Enter the width of the box (0 to exit):"))
            if width == 0:
                break
            height = int(input("Enter the height of the box (0 to exit):"))
            if height == 0:
                break

        except ValueError:
            print("Please enter an integer value")
        
        # Call box function with the user input