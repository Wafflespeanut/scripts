s="asbuddvbbsabcdeiewjgiwtuvwxyzxmn"
temp=s[0]; longstr=s[0]

for i in range(1,len(s)):
    if s[i]>=temp[-1]:
        temp+=s[i]
        if len(temp)>len(longstr):
            longstr=temp
    else: temp=s[i]
print "Longest substring in alphabetical order is:" +longstr
