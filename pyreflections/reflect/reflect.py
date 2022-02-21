import inspect


def get_user_attributes(cls):
    boring = dir(type('dummy', (object,), {}))
    attrs = {}
    bases = reversed(inspect.getmro(cls))   
    for base in bases:
        if hasattr(base, '__dict__'):
            attrs.update(base.__dict__)
        elif hasattr(base, '__slots__'):
            if hasattr(base, base.__slots__[0]): 
                # We're dealing with a non-string sequence or one char string
                for item in base.__slots__:
                    attrs[item] = getattr(base, item)
            else: 
                # We're dealing with a single identifier as a string
                attrs[base.__slots__] = getattr(base, base.__slots__)
    for key in boring:
        print(attrs[key]) 
        del attrs[key]  # we can be sure it will be present so no need to guard this
    return attrs