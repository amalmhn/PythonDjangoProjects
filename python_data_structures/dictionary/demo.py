students={
100:{'roll':100,'name':'ajay','total':140,'course':'bca'},
101:{'roll':101,'name':'vijay','total':145,'course':'bca'},
102:{'roll':102,'name':'anu','total':130,'course':'bca'},
103:{'roll':103,'name':'jinu','total':135,'course':'mca'},

}

print(students[100])
print(students[100]['name'])
print(students[100]['total'])

def printStudent(**kwarg):
    print(kwarg)
    id=kwarg.get('id')
    prop = kwarg.get('property')
    if(id in students):
        if prop in students[id]:
            print(students[id][prop])
        else:
            print("Details not available")

        print(students[id]['name'])
    else:
        print('student does not exist')


printStudent(id=100,property='course')
