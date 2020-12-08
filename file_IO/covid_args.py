f=open('complete.csv','r')

# 3st,6cured,7death,8confirm
covid_data={}

for lines in f:
    data=lines.rstrip('\n').split(',')
    state = data[1]
    cured = data[6]
    death = data[5]
    confirmed = data[4]


    if state not in covid_data:
        covid_data[state]={'state' : state,
                        'cured' : cured,
                        'death' : death,
                        'confirmed' : confirmed}
    else:
            covid_data[state]={'state': state,
             'cured': cured,
             'death': death,
             'confirmed': confirmed}

print(covid_data)

def print_covid_data(**kwargs):
    state=kwargs.get('state')
    if state in covid_data:
        print(state,covid_data[state]['confirmed'])
        if 'property' in kwargs:
            prop=kwargs.get('property')
            if prop in covid_data[state]:
                print(prop,covid_data[state][prop])
    else:
        print("There is no state with provided name")

print_covid_data(state='Kerala',property='death')