#!/usr/bin/env python
#
# Copyright author 2020
# Created by __sh0l1n@
#

def split(n):
    nSplited = clearZeros(n).split(".")
    nden = nSplited[0]
    nnum = nSplited[1] if len(nSplited) == 2 else ""
    return nden, nnum

def clearZeros(n):
    if n == "":
        return "0"

    nSplited = (n[1:len(n)] if n[0] == "-" else n).split(".")
    nden = nSplited[0]
    nnum = nSplited[1] if len(nSplited) == 2 else ""

    nDenFiltered, addZero = "", False
    for i in range(0, len(nden)):
        if nden[i]=="0":
            nDenFiltered += "0" if addZero else ""
        else:
            nDenFiltered += nden[i]
            addZero = True

    nDenFiltered = nDenFiltered if nDenFiltered!="" else "0"
    
    indexNnum, addZero = -1, False
    for i in range(len(nnum)-1, -1, -1):
        if nnum[i]!="0":
            indexNnum = i + 1
            break

    nResult = nDenFiltered
    if indexNnum != -1:
        nResult += "." + nnum[0:indexNnum]

    if nResult != "0":
        nResult = ("" if getSign(n)>0 else "-") + nResult
    return nResult

def fill(n0, n1, fillToRight=True):
    n0Len = len(n0)
    n1Len = len(n1)
    if n0Len > n1Len:
        n1Mod = n1
        diff = n0Len - n1Len
        for _ in range(0, diff):
            if fillToRight:
                n1Mod += "0"
            else:
                n1Mod = "0" + n1Mod
        return n0, n1Mod
    elif n0Len < n1Len:
        n0Mod = n0
        diff = n1Len - n0Len
        for _ in range(0, diff):
            if fillToRight:
                n0Mod += "0"
            else:
                n0Mod = "0" + n0Mod
        return n0Mod, n1
    else:
        return n0, n1

def getSign(n):
    return -1 if n[0]=="-" else 1

def getSplitedNumbers(a, b, fillZeros=True):
    aSign = getSign(a)
    bSign = getSign(b)
    aS = split(a if aSign>0 else a[1:len(a)])
    bS = split(b if bSign>0 else b[1:len(b)])
    denS = fill(aS[0], bS[0], fillToRight=False) if fillZeros else (aS[0], bS[0])
    numS = fill(aS[1], bS[1]) if fillZeros else (aS[1], bS[1])
    return (denS[0] + numS[0], len(aS[1]), aSign), (denS[1] + numS[1], len(bS[1]), bSign)

## Operations
### Sum
def __sumUnit(a, b, carryDefault = "0"):
    if len(a)!=len(b):
        return ["0", "0"]
    result = ""
    carry = carryDefault
    for i in range(len(a), 0, -1):
        index = i -1
        sum = int(a[index]) + int(b[index]) + int(carry)
        sumStr = str(sum)
        carry, sum = (sumStr[0], sumStr[1]) if len(sumStr)==2 else ("0", sumStr) 
        result = sum + result
    return result, carry    

def __sum(a, b):
    if len(a)!=3 or len(b)!=3:
        return "0"
    aFiltered, bFiltered = a[0], b[0]
    n, carry = "", "0"
    for i in range(len(aFiltered), 0, -1):
        index = i -1
        sum = int(aFiltered[index]) + int(bFiltered[index]) + int(carry)
        sumStr = str(sum)
        carry, sum = (sumStr[0], sumStr[1]) if len(sumStr)==2 else ("0", sumStr) 
        n = sum + n

    if carry != "0":
        n = carry + n

    decimals = max(a[1], b[1])
    nNat, nReal = n, ""
    if decimals != 0:
        nNat = n[0:len(n)-decimals]
        nReal = n[-decimals:]

    return nNat + "." + nReal

def sum(a, b, clear = True):
    aS, bS = getSplitedNumbers(a, b)
    result = "0"
    if aS[2]>0 and bS[2]>0:
        result =__sum(aS, bS)
    elif aS[2]>0 and bS[2]<0:
        result = __sub(aS, (bS[0], bS[1], 1))
    elif aS[2]<0 and bS[2]>0:
        result =__sub(bS, aS)
    elif aS[2]<0 and bS[2]<0:
        result ="-"+__sum(aS, bS)
    
    return clearZeros(result) if clear else result

## Sub
def __sub(a, b):
    if len(a)!=len(b):
        return ["0", "0"]
    
    aFiltered, bFiltered = (a[0], b[0]) if a>=b else (b[0], a[0])
    n, carry = "", "0"
    for i in range(len(aFiltered), 0, -1):
        index = i -1
        aInt = int(aFiltered[index])
        bInt = int(bFiltered[index]) + int(carry)
        aInt += 10 if aInt<bInt else 0
        sub = aInt - bInt
        n = str(sub) + n
        carry = "1" if int(aFiltered[index])<bInt else "0"
        
    sign = "-" if a[0]<b[0] else ""
    decimals = max(a[1], b[1])
    nNat, nReal = n, ""
    if decimals != 0:
        nNat = n[0:len(n)-decimals]
        nReal = n[-decimals:]

    return sign + nNat + "." + nReal
    
def sub(a, b, clear = True):
    aS, bS = getSplitedNumbers(a, b)
    result = "0"
    if aS[2]>0 and bS[2]>0:
        result = __sub(aS, bS)
    elif aS[2]>0 and bS[2]<0:
        result = __sum(aS, bS)
    elif aS[2]<0 and bS[2]>0:
        result = "-"+__sum(aS, bS)
    elif aS[2]<0 and bS[2]<0:
        result = __sub(bS, aS)
    
    return clearZeros(result) if clear else result

## Mul
def mul(a, b, clear = True):
    aS, bS = getSplitedNumbers(a, b)
    
    aFiltered, bFiltered = (aS[0], bS[0])
    sumStack = "0"
    for j in range(len(bFiltered), 0, -1):
        bindex = j - 1
        n, carry = "", "0"
        for i in range(len(aFiltered), 0, -1):
            index = i - 1
            aInt = int(aFiltered[index])
            bInt = int(bFiltered[bindex])
            mult = aInt*bInt + int(carry)
            n = str(mult%10) + n
            carry = str(int(mult/10))
        
        if carry != "0":
            n = carry + n

        for i in range(0, len(bFiltered) - j):
            n += "0"
        sumStack = sum(sumStack, n)
    
    # print("1.sumStack ..> " + sumStack)
    if aS[1]>0 or bS[1]>0:
        sumStackZerosIndex = -1
        for i in range(len(sumStack)-1, 0, -1):
            if sumStack[i] != "0":
                sumStackZerosIndex = i + 1
                break

        sumStack = sumStack[0: sumStackZerosIndex]

    # print("2.[cleanZeros]sumStack ..> " + sumStack)
    sign = "" if aS[2]==bS[2] else "-"
    decimals = aS[1] + bS[1]
    nNat = sumStack[0:len(sumStack)-decimals]
    # print("decimals " + str(decimals))
    # print("nNat ..> " + nNat)
    nReal = "" if decimals==0 else sumStack[-decimals:]
    # print("nReal ..> " + nReal)
    sumStack = sign + nNat + "." + nReal
    # print(sign)
    # print(a)
    # print(b)
    # print("3.sumStack ..> " + sumStack)
    
    return clearZeros(sumStack) if clear else sumStack

def pow(a, e, clear = True):
    exp = clearZeros(e)
    if exp<"0":
        ## TODO: sqrt
        return "0.0"
    if exp=="0":
        return "1"
    elif exp=="1":
        return a
    else:
        powStack = a
        for i in range(1, int(float(exp))):
            powStack = mul(powStack, a, False)
    
    return clearZeros(powStack) if clear else powStack

## div
def div(a, b, clear = True):
    print("### DIVIDE " + a + " / " + b)

    if a == "0":
        return "NaN"
    elif b == "0":
        return "0"
    
    aS, bS = getSplitedNumbers(a, b, False)
    
    aSplitted = split(a)
    bSplitted = split(b)
    aFiltered, bFiltered = (aS[0], bSplitted[0]+bSplitted[1])

    print("### DIVIDE " + aFiltered + " / " + bFiltered)

    
    decimalIndex = -1#len(aSplitted[0]) if len(aSplitted[0])>0 else -1
    extraDecimals = -1

    divStack = ""
    modStack = ""
    iteCount = 0

    while aFiltered!="":
        # if iteCount == 100:
        #     break
        print("###### START ITE --> " + aFiltered + " ######################################################3")

        decimalIndex = len(divStack) if len(aFiltered)<=len(aSplitted[1]) and decimalIndex==-1 else decimalIndex

        compareResult = -1
        stepDivid = ""
        print("0.stepDiv: " + stepDivid + " aFiltered: " + aFiltered + " divStack " + divStack + " modStack " + modStack)
        #if stepDivid != "0":
        while compareResult == -1:
            
            stepDivid += aFiltered[0]
            aFiltered = aFiltered[1:]

            print("compare b " + bFiltered + " with " + stepDivid + " and afi " + aFiltered + " divstack " + divStack)
            compareResult = compare(stepDivid, bFiltered)
            if compareResult == -1 or stepDivid == "0":
                print("compare result -1")
                if stepDivid == "0":
                    print("stepDivid == 0")
                    divStack += "0"
                    break
                else:
                    print("stepDivid != 0")
                    divStack += "0"
                    if aFiltered == "":
                        aFiltered = "0" + aFiltered


                    
                # elif aFiltered == "":
                #     print("addZero")
                #     aFiltered += "0"
                #     divStack += "0"
                #     stepDivid += "0"
            
                decimalIndex = len(divStack) if len(aFiltered)<=len(aSplitted[1]) and decimalIndex==-1 else decimalIndex
                    # divStack += "0"
                
            #     stepDivid += aFiltered[0]
            #     aFiltered = aFiltered[1:]
            # if aFiltered=="":
            #         break
        # else:
        #     divStack += "0"
        
        print("1.divsTack " + divStack + " stepDiv: " + stepDivid + " aFiltered: " + aFiltered + " decimalIndex " + str(decimalIndex))
        if compareResult == 0:
            print("---------------> compare result 0 and is " + str(compareResult))
            divStack += "1"
        elif compareResult == 1:
            print("---------------> compare result 1 and is " + str(compareResult))
            for m in range(1, 10):
                mResult = mul(bFiltered, str(m))
                # print("mResult " + mResult)
                compareResult = compare(mResult, stepDivid)
                if compareResult == 0:
                    # print("= m " + str(m))
                    divStack += str(m)
                    modStack = ""
                    break
                elif compareResult == 1:
                    # print("> m " + str(m))
                    divResult = str(m-1)
                    divStack += divResult
                    modStack = sub(stepDivid, mul(bFiltered, divResult))
                    modStack = modStack if modStack != "0" else ""
                    # modResult = sub(stepDivid, mul(bFiltered, divResult))
                    break
        print("11. divstack end iteration ----> "  + divStack + " modStack: " + modStack + " decimalIndex " + str(decimalIndex) + " iteCount " + str(iteCount))
        aFiltered = modStack + aFiltered
        print("22. divstack end iteration ----> "  + divStack + " modStack: " + modStack + " decimalIndex " + str(decimalIndex) + " iteCount " + str(iteCount))
        iteCount += 1    
#     >>> "06"[0:1]
# '0'
# >>> "06"[1:]
# '6'
    sign = "" if aS[2]==bS[2] else "-"
    # denLength = len(divStack) if decimalIndex==-1 else len(divStack)-decimalIndex
    # nNat = divStack if decimalIndex==-1 else divStack[0:decimalIndex]
    # nNat = nNat if nNat!="" else "0"
    # print("nNat " + nNat)
    # nReal = "0" if decimalIndex==-1 else divStack[decimalIndex:len(divStack)]
    # print("nReal " + nReal)
    # divStack = sign + nNat + "." + nReal
    return divStack
    # while True:
    #     print("######### next ite " + str(i) + " divStack " + divStack + " modStack " + modStack)
    #     # if divStack!="" and  (modStack == "" or modStack == "0"):
    #     #     break
    #     if modStack == "" and i>=len(aFiltered):
    #         print("go out on " + str(i))
    #         break

    #     acc = modStack + aFiltered[i] if i<len(aFiltered) else "0"
    #     modStack = ""

    #     print("acc " + acc + " bFiltered: " + bFiltered)
    #     # acc = modStack + (aFiltered[i] if i<len(aFiltered) else "0")
    #     extraDecimals += (0 if i<len(aFiltered) else 1)
    #     # modStack = ""
    #     if modStack == "" and i>=len(aFiltered):
    #         break
    #     if compare(acc, bFiltered) == -1:
    #         while compare(acc, bFiltered) == -1:
    #             print("compare acc " + acc + " bfil " + bFiltered + " com " + str(compare(acc, bFiltered)))
    #             i+=1 

    #             if i<len(aFiltered):
    #                 acc += aFiltered[i]
    #             # elif acc == "0" and i>=len(aFiltered)-1:
    #             #     divStack += "0"
    #             #     break
    #             else:
    #                 print("add zero")
    #                 acc += "0"
    #                 divStack += "0"
    #                 extraDecimals += 1
    #                 decimalIndex = i if decimalIndex==-1 else decimalIndex
                
    #         print("after filt " + acc + " extraDe " + str(extraDecimals) + " decimalIndex " + str(decimalIndex))

    #     if compare(acc, bFiltered) == 0: #acc<bFiltered
    #         print("its same number so 1")
    #         divStack += "1"
    #     elif compare(acc, bFiltered) == 1: #acc>bFiltered
    #         print("divide " + acc)
    #         divResult, modResult = "", ""
    #         for m in range(1, 11):
    #             mResult = mul(bFiltered, str(m))
    #             compareResult = compare(mResult, acc)
    #             if compareResult == 0:
    #                 print("=")
    #                 divResult, modResult = str(m), "0"
    #                 break
    #             elif compareResult == 1:
    #                 print(">")
    #                 print("m " + str(m))
    #                 divResult = str(m-1)
    #                 modResult = sub(acc, mul(bFiltered, divResult))
    #                 break
            
    #         divStack += divResult
    #         modStack += modResult
    #         print("divResult: " + divResult + " modResult: " + modResult + " divStack " + divStack)
    #     #acc = ""
    #     i+=1
        
    # #for i in range(0, len(a)):

    #     #i+=1
        

    # print("################ FINISHED")
    # print(aS + bS)
    # print("decimalIndex: " + str(decimalIndex))
    # print("extraDecimal: " + str(extraDecimals))
    # print("AFTER filter divStack " + divStack)
    
    # #1. Comprar si divisor cabe en dividendo, cojer un una porcion del dividendo igual a la longiuted del divisor
    

    # #2. Empezar probar multiplicaciones hasta que X se pase, entonces es X-1
    # #3. Multiiplicar dividor por X-1 y restar porcion cojida a ese numero
    # #4. Resto, y volver a empezar en 1

    # sign = "" if aS[2]==bS[2] else "-"
    # nNat = divStack[0:decimalIndex]
    # nNat = nNat if nNat!="" else "0"
    # nReal = "0" if decimalIndex==-1 else divStack[decimalIndex:len(divStack)]
    # divStack = sign + nNat + "." + nReal
    # return divStack
    # #return clearZeros(divStack) if clear else divStack

## Compare two string numbers
# -1: a<b, 0: a==b, 1: a>b
def compare(a, b):
    if a == b:
        return 0

    aS,bS = split(a),split(b)
    adS, bdS = fill(aS[0], bS[0], fillToRight=False)
    ##TODO: Unifiy code below for natural and decimals
    for i in range(0, len(adS)):
        aInt = int(adS[i])
        bInt = int(bdS[i])
        if aInt<bInt:
            return -1
        elif aInt>bInt:
            return 1

    adS, bdS = fill(aS[1], bS[1])
    for i in range(0, len(adS)):
        aInt = int(adS[i])
        bInt = int(bdS[i])
        if aInt<bInt:
            return -1
        elif aInt>bInt:
            return 1
    
    return 0