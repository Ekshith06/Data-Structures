""" Python Script to find minimum among three numbers """

e = int(input("get the 1st number"))
k = int(input("get the 2nd number"))
s = int(input("get the 3rd number"))
if e>k and e>s:
  print(e,"is greater")
elif k>e and k>s:
  print(k,"is greater")
elif s>k and s>e:
  print(s,"is greater" )
