import re

st = "2017-2018"
#print re.findall(r'([+-]?\d+\.\d+)',myString).group()
x1=st.split("-")[0]
x2=st.split("-")[1]
print (x1+x2)
