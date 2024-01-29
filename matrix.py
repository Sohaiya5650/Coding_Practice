row1 = int(input("Enter number of rows: "))
col1 = int(input("Enter number of columns: "))


matrix1 = []


for i in range(row1):
    row_input1 = []
    for j in range(col1):
        row_input1.append(int(input()))
    matrix1.append(row_input1)


for i in range(row1):
    for j in range(col1):
        print(matrix1[i][j], end=' ')
    print()



row2 = int(input("Enter number of rows: "))
col2 = int(input("Enter number of columns: "))

matrix2 = []

for i in range(row2):
    row_input2 = []
    for j in range(col2):
        row_input2.append(int(input()))
    matrix2.append(row_input2)

# for i in range(row1):
#     for j in range(col1):
#         print(matrix1[i][j], end=' ')
#     print()


for i in range(row2):
    for j in range(col2):
        print(matrix2[i][j], end=' ')
    print()


print('Select your operation: ')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')

user_input = input('Enter your option(1,2,3): ')

if user_input == '1':
    if row1==row2 and col1==col2:
        result_add = []
        for i in range(row1):
            row_add = []
            for j in range(col1):
                row_add.append(matrix1[i][j] + matrix2[i][j])
            result_add.append(row_add)

        print('Result of addition is: ')
        for i in range(row1):
            for j in range(col1):
                print(result_add[i][j], end=' ')
            print()
    
    else:
        print('Number of rows and columns do not match')


elif user_input == '2':
    if row1==row2 and col1==col2:
        result_sub = []
        for i in range(row1):
            row_sub = []
            for j in range(col1):
                row_sub.append(matrix1[i][j] - matrix2[i][j])
            result_sub.append(row_sub)

        print('Result of subtraction is: ')
        for i in range(row1):
            for j in range(col1):
                print(result_sub[i][j], end=' ')
            print()
    else:
        print('Number of rows and columns do not match')

elif user_input == '3':
    if col1==row2 :
        result_mult = []
        for i in range(row1):
            row_mult = []
            for j in range(col2):
                el_sum = 0
                for k in range(col1):
                    el_sum = el_sum + matrix1[i][k] * matrix2[k][j]
                row_mult.append(el_sum)
            result_mult.append(row_mult)

        print('Result of multiplication is: ')
        for i in range(row1):
            for j in range(col1):
                print(result_mult[i][j], end=' ')
            print()
    else:
        print('Number of 1st columns and 2nd rows do not match')
