# La relación “sigue a” no es simétrica, ya que una persona no tiene porqué seguir a
# sus seguidores. No obstante, a veces ocurre que una persona sigue a la persona que
# lo sigue. Es decir, si PersonaA sigue a PersonaB, entonces PersonaB sigue a
# PersonaA. Con este ejercicio queremos identificar los pares (PersonaA, PersonaB)
# que no tienen una relación (PersonaB, PersonaA) definida. Con los mismos datos
# anteriores, describe el algoritmo MapReduce que permite obtener la lista de las
# relaciones que cumplen dicha condición.
import functools

red_social = [('Alicia', 'Benito'), ('Benito', 'Alicia'),
('Carlos', 'Benito'), ('Benito', 'Carlos'),
('Daniela', 'Enrique'), ('Enrique', 'Francisco'),
('Francisco', 'Enrique'), ('Daniela', 'Benito')]

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

def _transform(x):
    x_sort = list(x)
    x_sort.sort()
    key  = x_sort[0]+x_sort[1]
    return (key,x)

if __name__ == "__main__":
    mapped = map(_transform , red_social)
    mapped = list(mapped)
    keys = set(i[0] for i in mapped)
    shuffle = _shuffle(mapped,keys)
    #print(list(shuffle))
    reduced = [functools.reduce(lambda a,b: False if len(b) > 1 else b, i[1]) for i in shuffle]
    print(reduced)