user_input = int(input("Insert the number: "))
# even_sum = 0
# for number in range(2, user_input + 1, 2):
#     even_sum += number
# print(even_sum)

# another way to get it
alternative_sum = 0
for number in range(1, user_input + 1):
    if number % 2 == 0:
        alternative_sum += number

print(alternative_sum)
