def DegreeTransfer(degree, unit):
    if unit == "C" or unit == "c":
        degreeF = degree * (9/5) + 32
        degreeC = float(degree)
    elif unit == "F" or unit == "f":
        degreeC = (5/9) * (degree - 32)
        degreeF = float(degree)
    else:
        print("輸入值有誤，請重新輸入")
        return
    print("華氏"+str(degreeF)+"℉、攝氏"+str(degreeC)+"℃")

inputDegree, inputUnit = input("請輸入溫度與單位，例如攝氏25度c可輸入'25 c'").split()
DegreeTransfer(eval(inputDegree), inputUnit)

