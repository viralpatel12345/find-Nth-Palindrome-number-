def isPalindrome(num) :
    num1=num
    rem=0
    reverse=0
    while num!=0 :
        rem=int(num%10)
        num=int(num/10)
        reverse=reverse*10+rem

    if(num1 == reverse) :
        return True
    else:
        return False

val=int(input("\nwhich Palindrome You Want ?  : "))
c=0
PalindromeList=[]

for i in range(0,1000000) :
    if isPalindrome(i) :
        c=c+1
        PalindromeList=PalindromeList+[i]
        if c==val :
           break

print("Palindrome List = {}".format(PalindromeList))
print("Palindrome for Position {} = {}".format(val,PalindromeList[val-1]))
print("Length Of Palindrome List = {}".format(len(PalindromeList)))