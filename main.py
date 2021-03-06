#Asher Lasday
#SoftDev2 pd8
#HW10 -- How Strong?
#2017-04-23

def passCheck(pw):
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '012345789'
    
    lowBoo = len([x for x in pw if x in lowers]) != 0
    highBoo = len([x for x in pw if x in uppers]) != 0
    numsBoo = len([x for x in pw if x in nums]) != 0
    return (lowBoo and highBoo and numsBoo)

print passCheck("CLASSIC")
print passCheck("classic")
print passCheck("123")
print passCheck("clAssic")
print passCheck("class1c")
print passCheck("CL4SSIC")
print passCheck("C1assic")

def rating(pw):
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '012345789'
    specs = ".?!&#,;:-_*"

    rat = 0

    if (len([x for x in pw if x in lowers]) != 0): rat+=1
    if (len([x for x in pw if x in uppers]) != 0): rat+=1
    if (len([x for x in pw if x in nums]) != 0): rat+=1
    if (len([x for x in pw if x in specs]) != 0): rat+=1
    
    return rat



print rating("CLASSIC")
print rating("classic")
print rating("123")
print rating("clAssic")
print rating("class1c")
print rating("CL4SSIC")
print rating("C1assic")
print rating("C1ass.#")
print rating("C1assi&")
