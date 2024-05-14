s = (input())
i = 0
j = len(s)
k = 0
d = 0

while i != j:
   if "a" <= s[i] <= "z" or "A" <= s[i] <= "Z" or s[i] == " ":
      i = i + 1
   else:
      j = i

j = j + 1
while j < len(s):
   if "a" <= s[j] <= "z" or "A" <= s[j] <= "Z" or s[j] == " ":
      k = j
      j = len(s)
      #print(s[i:k], i)
   else:
      j = j + 1

while k != j:
   if "a" <= s[k] <= "z" or "A" <= s[k] <= "Z" or s[k] == " ":
      k = k + 1
   else:
      j = k

k = j
while j != i:
   if "a" <= s[j] <= "z" or "A" <= s[j] <= "Z" or s[j] == " ":
      i = j
      print(s[k:i], k)
   else:
      j = j + 1
