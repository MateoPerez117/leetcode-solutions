# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

chars = ["a"]
read = 0
write = 0

while read < len(chars):
    contador = 1

    while read < len(chars) - 1 and chars[read] == chars[read + 1]:
        contador += 1
        read += 1

    chars[write] = chars[read]
    write += 1

    if contador > 1:
        for i in str(contador):
            chars[write] = i
            write += 1
    read += 1

print (chars)