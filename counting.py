def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            
            return count

occurrences('azcbobobegghakl', 'bob')

def find(string, sub):
    count = 0
    for i in range(len(string)):
        if string[i:i+3]== sub:
            count += 1
    print(count)
        
find('azcbobobegghbob', 'bob')            

def longest(s):
    l = []
    new_s = ""
    
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            if s[i] not in new_s:
               new_s += s[i]
               new_s += s[i+1]
               
               
            else:
                new_s += s[i+1]
                
                
        
            l.append(new_s)
        else:
            l.append(max(s))
            new_s = ""
        
        
    print("Longest substring in alphabetical order is: " + max(l, key=len))
    
        

longest('zyxwvutsrqponmlkjihgfedcba')
