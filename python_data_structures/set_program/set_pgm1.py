st=set()
st1=set()
print(type(st))

st={10,20,30,40,45,30,40,50}
st1={40,50,60,70,80,90,100}

union=st.union(st1)
print(union)
update=st.update(st1)
print(st)
intersec=st.intersection(st1)
print(intersec)
dif=st.difference(st1)
print(dif)
