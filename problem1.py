total = 0; 
# function returning binary string
def bin_convert(n):
    #using bin() for binary conversion
    bin1 = bin(n)
    # removing "0b" prefix 
    binary = bin1[2:]
    return binary

#function returning palindrome string
def palin(string):
    #reversing string using slicing method one step backward
    reverse_string = string[::-1]
    if reverse_string == string:
        return True
    else:
        return False

for i in range(0,1000000):
    #val stores palindrome decimals
    val = palin(str(i))
    binary = bin_convert(i)
    #val2 stores binary palindromes
    val2 = palin(str(binary))
    if val == True and val2 == True:
        total = total + i

print (total)
