# A program to print boxes to the command line

# TODO: is_edge function: check if point is on box edge
# TODO: print_box function: print box with given dimensions

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

        # Call print_box function with dimensions
