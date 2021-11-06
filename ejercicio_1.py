# Suponer los datos de una red social que consisten en un conjunto de pares del tipo
# (personaA, personaB) que representan una relación “sigue a” (‘following’) de forma que
# la personaA sigue a la personaB. Dado el siguiente conjunto de datos,describe el
# algoritmo MapReduce que calcula el número de seguidores que tiene cada persona.
import functools

red_social = [('Alicia', 'Benito'), ('Benito', 'Alicia'),
('Carlos', 'Benito'), ('Benito', 'Carlos'),
('Daniela', 'Enrique'), ('Enrique', 'Francisco'),
('Francisco', 'Enrique'), ('Daniela', 'Benito')]

def _transform(x):
    return (x[1],1)

def _shuffle(mapped,keys):
    first_tuple_elements = [a_tuple[0] for a_tuple in mapped]
    values = []
    for key in keys:
        elements = []
        index = 0
        while index != -1:
            try:
                index = first_tuple_elements.index(key)
                tuple_element = mapped.pop(index)
                first_tuple_elements.pop(index)
                elements.append(tuple_element[1])
            except:
                index = -1
        if len(elements) > 0:
            values.append(elements)
        else:
            values.append([0])
    shuffle = zip(keys,values)
    return shuffle

if __name__ == "__main__":
    mapped = map(_transform , red_social)
    mapped = list(mapped)
    keys = set(i[0] for i in red_social)
    shuffle = _shuffle(mapped, keys)
    reduced = [functools.reduce(lambda a,b: a+b, i[1]) for i in shuffle]
    result = zip(keys,reduced)
    print(list(result))