D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

for id, info in D.items():
    print("\nEmployee ID:", id)
    for key in info: #for every value print the key
        print(key + ':', info[key])

# Prints Employee ID: emp1
#        name: Bob
#        job: Mgr

#        Employee ID: emp2
#        name: Kim
#        job: Dev

#        Employee ID: emp3
#        name: Sam
#        job: Dev