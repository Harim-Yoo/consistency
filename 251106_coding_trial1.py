All positive integers are written consecutively (starting from 1) as a single sequence of decimal digits. Find the $2025$th digit in that sequence.

nums = list(range(1,1000))
string = "".join(map(str,nums))
print(string[2024])
