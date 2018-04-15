# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
# So "xxyz" counts but "x.xyz" does not.

#Ex:  xyz_there('abcxyz') → True
#     xyz_there('abc.xyz') → False
#     xyz_there('xyz.abc') → True

def xyz_there(str):
  #Assume there is no 'xyz' in the string initially
  flag = False
  
  #Check if 'xyz' is part of the string
  if 'xyz' in str:
    for i in range (len(str)):
      #Check if 'xyz' is preceded by '.'
      if (str[i] == 'x' and str[i-1] !='.'):
        flag = True
      
  return flag
