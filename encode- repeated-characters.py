# Given a string with a lot of repeated characters, eg. "aaabbdcccaaaa", 
# write some code that can encode it such that the character repetition 
# is represented as a number instead: "3a2b1d3c4a".

s = "aaabbdcccaaaa"
new_string = ""
count = 1 

for i in range(len(s)-1):
  temp = s[i]

  # Is next char the same as current?
  if s[i+1] == temp:
    count+=1     

  # Not the same
  else:
    new_string += str(count) + temp
    count = 1
    
new_string += str(count) + temp   
print(new_string)
