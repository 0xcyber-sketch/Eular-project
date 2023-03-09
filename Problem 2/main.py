

fibValue = 0
oldValue= 0 
newValue = 1
result = 0

while fibValue < 4000000:
  if fibValue % 2 == 0:
    result = result + fibValue
  fibValue =  oldValue + newValue
  oldValue = newValue
  newValue = fibValue
  
print(result)

##Solution 4613732