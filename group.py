"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
my_group=
    my_group = {
                    'name':'',
                        'age':'',
                        'job':'' }
                   
    Jill = {'name':'Jill',
                'age':'26',
                'job': 'Biologist'}
    Zalika = {'name':'Zalika',
                'age':'28',
                'job': 'Artist'}
    John = {'name':'John',
                'age':'27',
                'job': 'writer'}
    Nash = {'name':'Nash',
                'age':'34',
                'job': 'Chef'}
        






"""
Create an example instance, in an editor or a notebook, of a structure for this group:

Jill is 26, a biologist and she is Zalika's friend and John's partner.
Zalika is 28, an artist, and Jill's friend
John is 27, a writer, and Jill's partner.
Nash is 34, a chef, John's cousin and Zalika's landlord.
Some things you may wish to consider in your model:

Does it allow people who have no job?
Does it allow people with no connections?
Does it assume that connections are always reciprocal (e.g. if A is B's friend, does B automatically consider A a friend too?)

"""
"""
my_group =
my_group = {
    'Jill' : {
        'age'           : 26,
        'job'           : 'biologist',
        'connections'   : {
            'Jill'      : ['self'],
            'Zalika'    : ['friend'],
            'John'      : ['partner'],
            'Nash'      : []  
        }
    },
    'Zalika' : {
        'age'           : 28,
        'job'           : 'artist',
        'connections'   : {
            'Jill'      : ['friend'],
            'Zalika'    : ['self'],
            'John'      : [],
            'Nash'      : []  
        }
    },
    'John' : {
        'age'           : 27,
        'job'           : 'writer',
        'connections'   : {
            'Jill'      : ['partner'],
            'Zalika'    : [],
            'John'      : ['self'],
            'Nash'      : ['cousin']  
        }
    },
    'Nash' : {
        'age'           : 34,
        'job'           : 'chef',
        'connections'   : {
            'Jill'      : [],
            'Zalika'    : ['landlord'],
            'John'      : ['cousin'],
            'Nash'      : ['self']  
        }
    }
}

print(my_group) 
"""