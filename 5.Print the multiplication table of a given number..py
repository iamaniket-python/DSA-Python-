# Print the multiplication table of a given number

num=int(input("Enter a number="))
def print_table(n, i=1):
    if i<=10:
        print(f"{n} X {i} ={n * i}")
        print_table(n, i+1)

print(f"\n--- Multiplication Table for {num} ---")
print_table(num)

# Output:
# 5 X 1 =5
# 5 X 2 =10
# 5 X 3 =15
# 5 X 4 =20
# 5 X 5 =25
# 5 X 6 =30
# 5 X 7 =35
# 5 X 8 =40
# 5 X 9 =45
# 5 X 10 =50