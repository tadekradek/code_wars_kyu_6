def to_camel_case(text):
    try:
        output =""
        if text[0].isupper() == True:
            output = text.replace("-"," ").replace("_"," ").title().replace(" ","")
        else:
            output = text.replace("-"," ").replace("_"," ").title().replace(" ","")
            output = output[0].lower() + output[1:]
        return output
    except:
        return text


# very not optimal solution, but at least works

# another solutions

"""
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '') # very smart, cut the first letter no matter what, and perform operations on the rest


def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

"""