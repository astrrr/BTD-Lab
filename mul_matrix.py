size_matrix_a = input()
size_matrix_b = input()

matrix_a = []
matrix_b = []
result = []

#add matrix
#input per row  index 0 = row , index 1 = column
for i in range(int(size_matrix_a.split()[0])) :
    matrix_a.append(input())

for i in range(int(size_matrix_b.split()[0])):
    matrix_b.append(input())

#now we have 2 matrix

#check size of matrix if cant mult -> print cant calculate
if (size_matrix_a.split()[-1] != size_matrix_b.split()[0]):
    print('Cant calculate !')

elif (size_matrix_a.split()[-1] == size_matrix_b.split()[0]):
    #ได้ขนาด list ของคำตอบละ ค่อยหาวิธีวนลูปเอาของแต่ละ matrix มาคูณบวก 
    for i in range((int(size_matrix_a.split()[-1]))*(int(size_matrix_b.split()[0]))):
        #เอาตำแหน่งของแต่ละตัวมา operate กัน 
        row_a = matrix_a.split()
        for index in row_a :
            print(index)

    