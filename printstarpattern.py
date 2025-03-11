def right_angle_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def inverted_right_angle_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def diamond(n):
    pyramid(n)
    inverted_pyramid(n - 1)

def main():
    n = int(input("Enter the number of rows: "))
    print("\nRight Angle Triangle:")
    right_angle_triangle(n)
    
    print("\nInverted Right Angle Triangle:")
    inverted_right_angle_triangle(n)
    
    print("\nPyramid:")
    pyramid(n)
    
    print("\nInverted Pyramid:")
    inverted_pyramid(n)
    
    print("\nDiamond:")
    diamond(n)

if __name__ == "__main__":
    main()
