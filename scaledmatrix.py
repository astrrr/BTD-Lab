max_list = 0.0000
min_list = 0.0000

column = int(input())
row = int(input())

pre_scale_data = []
scaled_data =[]

for i in range(column*row):
    pre_scale_data.append(float(input()))


min_list = min(pre_scale_data) *(-1)


max_list = max(pre_scale_data)


scaler = 1/(max_list + min_list)


for i in pre_scale_data:
    scaled_data.append((i+min_list)*scaler)

print(scaled_data)
result = []
for i in range(row):
    temp = []
    for j in range(column):
        temp.append("%.4f" % scaled_data.pop(0)) 
    
    result.append(temp)
    temp = []

for i in range(row):
    print(*result[i])