in1 = input().split()
in2 = input().split()

result = []

if len(in1) != len(in2):
    print("Invalid")

else :
    for i in range(len(in1)):
        if int(in1[i]) + int(in2[i]):
            print("Invalid")
            break
        elif int(in1[i]) or int(in2[i]) > 32548 :
            print("Invalid")
            break
        else:
            result.append(int(in1[i]) + int(in2[i]))
    print(*result)