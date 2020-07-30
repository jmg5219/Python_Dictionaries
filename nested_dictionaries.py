digital_crafts = {
    'US' : { 
        'Georgia': {
            'Atlanta':'3423 Piedmont Road NE #420'
        },
        'Texas' : {
            'Houston': '3302 Canal St.'
        }
    }
    
}
# Nested dictionary
print(digital_crafts['US']['Georgia']['Atlanta'])
# Adding a dictionary
digital_crafts['US']['Florida'] = {
    'Tampa' : '1234 That Tampa Place'
}
#Print after adding to nested dictionary
print(digital_crafts['US']['Florida']['Tampa'])
