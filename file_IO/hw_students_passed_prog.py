file1=open('hw_students','r')
file2=open('hw_passed','r')

st=set()
st2=set()

for i in file1:
    st.add(i.rstrip('\n'))
print(st)

for j in file2:
    st2.add(j.rstrip('\n'))
print(st2)

print('--------------------------------------------')
failed=st.difference(st2)

print(failed)