from itertools import product
import tema_problema1_header

k=1 #With these variables we will form the menu
M = list()
print(tema_problema1_header.building(M)) #We are making the list
x = list(product(M, M)) #We make the cartesian product

#Menu
while k != 0:
    k =int(input("""Choose an option:
1.Display cartesian product and verify binary relationship
2.Equivalence classes
3.Transient closure
4.Exit
"""))
    if k == 1:
        print(tema_problema1_header.display(x))
        tema_problema1_header.binary_relationship(x)
    elif k == 2:
        new_class = []
        new_class = tema_problema1_header.equivalent_classes(M)
        print (new_class)
    elif k == 3:
        print("Transient closure :")
        print(tema_problema1_header.transient_closure(x))
    elif k == 4:
        break

