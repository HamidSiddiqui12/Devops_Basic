s= "****** hello world ******"  #Expected output: Hello World
result = s.strip('*').strip().title()
print(s,"\n",result)  
# or print(s,result, sep = '/ ')  ----> "sep" can be anything(/, \n, |, etc) with which you want to separate both the variables.
print(len(s), len(result))