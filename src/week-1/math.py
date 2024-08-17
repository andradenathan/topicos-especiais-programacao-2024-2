n = int(input())

power_2_last_digit = [2, 4, 8, 6]
power_3_last_digit = [3, 9, 7, 1]
power_4_last_digit = [4, 6]

list_size_4_index = (n % 4) - 1
list_size_2_index = (n % 2) - 1

result = (1 + 
          power_2_last_digit[list_size_4_index] + 
          power_3_last_digit[list_size_4_index] + 
          power_4_last_digit[list_size_2_index]) % 5

print(result)