from random import randint

#We build the M set with a for and then use the "append" function to add items to the list
def building(a):
    numbers_elements = int(input("Enter how many elements you want in M:")) #the number of items in the list
    print('Enter numbers in M: ')
    for item in range(int(numbers_elements)):
        n = input("element :") #introduction of the element
        a.append(int(n)) #the function that adds items to the list
    return a

#the function that display the set
def display(crowd):
    return crowd

#See it's reflexive
#A relation "Crowd" is called reflexive when:
#∀ a ∈ Set, (a,a) ∈ Crowd
def is_reflexive(crowd):
    new_set = [(a, b) for a in crowd for b in crowd if a == b]
    for item in range(int(len(new_set))):
        if new_set[item] in crowd:
            return False
    return True

#See it's tranzitive
#A relation "Crowd" is called transitive when:
#∀ (a, b) ∈ Crowd, (b, c) ∈ Crowd ==> (a, c) ∈ Crowd
def is_tranzitive(crowd):
    for a, b in crowd:
        for c, d in crowd:
            if b == c and ((a, d) not in crowd):
                return False
    return True

#See it's symetric
#A relation "Crowd" is called symetric when:
#∀ (a, b) ∈ Crowd, (b, a) ∈ Crowd
def is_symmetric(crowd):
    if all(sset[::-1] in crowd for sset in crowd):
        return True
    return False

#If is reflexive,tranzitive and symetric it results that the relationship is binary
def binary_relationship(crowd):
    a = is_reflexive(crowd)
    b = is_tranzitive(crowd)
    c = is_symmetric(crowd)
    if a and b and c:
        print("The relationship is binary")
    else:
        print("The relationship is not binary")

#The random variable represents the number of partitions in which the classes are divided,for example the first class contains the elements with rest 0,the second rest 1 and so on
random_variable = randint(0, 9)
print("random variable: ", random_variable)

#equivalence classes divide into partition
def equivalent_classes(crowd):
    def rel(l1, l2):
        return l1 % random_variable == l2 % random_variable

    echivalentclass = [] #Found partitions

    for x in crowd: #Loop over each element
        for item in echivalentclass:
            if rel(x, item[0]): #Found a partition for it!
                item.append(x)
                break
        else:
            echivalentclass.append([x]) #Make a new partition for it
    return echivalentclass

#if in the original list we have two tuples form (a,b) and (c,d) ,and b equals c ,then we add tuple (a,d).
def transient_closure(crowd):
    closure = set(crowd)
    while True:
        new_set = [(a, d) for a, b in closure for c, d in closure if b == c]
        # print(new_set)
        pair_formed = set(new_set)
        crowd2 = closure | pair_formed
        if crowd2 == closure:
            break
        closure = pair_formed
    return closure
