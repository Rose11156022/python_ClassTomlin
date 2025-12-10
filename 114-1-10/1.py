n_str = input().strip()
length = len(n_str)

for i in range(length + 1):
    temp_str = n_str[:i] + '3' + n_str[i:]
    
    for j in range(len(temp_str) + 1):
        final_str = temp_str[:j] + '5' + temp_str[j:]
        
        val = int(final_str)
        
        if val % 21 == 0:
            print(1)
            exit()

print(0)