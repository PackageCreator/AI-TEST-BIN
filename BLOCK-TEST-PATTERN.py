def patterns():
    num = 0
    in1 = [1, 4, 5, 2]
    in2 = [10, 2, 6, 11]
    nums = max(in2)
    for i in range(nums):
        if in1[num] in in2:
            print(in1[num])
            found = True
            break
        else:
            num += 1
    def gapsAVG():
        # Even thought we can now recognise patterns to predict the next number we have to find the gap
        numcount = 0
        numcount2 = 0
        if found == True:
            print("{", in1 + "[]" + in2, "}")
            if in1[numcount] + numcount == in1[numcount2]:
                numcount += 1
                numcount2 += 1
    gapsAVG()    
patterns()