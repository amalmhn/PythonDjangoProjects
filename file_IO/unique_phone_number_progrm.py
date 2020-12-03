file=open('data','r') #reference #default mode is r
st=set()

for numbers in file:
    st.add(numbers.rstrip('\n'))

print(st)


