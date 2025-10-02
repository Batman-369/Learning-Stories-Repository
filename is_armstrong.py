def is_armstrong(num):
    power = len(str(num))
    total = sum(int(digit) ** power for digit in str(num))
    return num == total

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(f"Armstrong numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_armstrong(num):
        print(num)
