
key = int(input())
num_chrs = int(input())
decrypted_msg = ""

for i in range (0, num_chrs):
    char = input()
    new_chr = chr(ord(char) + key)
    decrypted_msg += new_chr
    
print (decrypted_msg)

