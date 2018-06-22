from itertools import product #From the itertools libraries we choose the product that helps us calculate the cartesian product


class myList(object): #my class
    set2 = {} #global variable
    def __init__(self):
        self.a = [] #We have the builder a empty

    # We build the M set with a for and then use the "append" function to add items to the list
    def newList(self):
        numbers_elements = int(input("Enter how many elements you want in M:"))  # the number of items in the list
        print('Enter numbers in M: ') #Enter a number
        for item in range(int(numbers_elements)):
            n = input("element[{}]:" .format(item))#introduction of the element
            self.a.append(n)#the function that adds items to the list
        return self.a
    #We make the cartesian product of the sets a
    def cartesian_product(self):
        p = list(product(self.a, self.a))
        return p
    #We check that the relationship is transitive
    # A relation is called transitive when:
    # ∀ (a, b) ∈ cartesian product, (b, c) ∈ cartesian product ==> (a, c) ∈ cartesian product
    def tranzitive(self):
        global set2 #we use global variable
        new_relation = [] #empty list which we will use
        for a, b in self.cartesian_product():
            for c, d in self.cartesian_product() :
                new_relation.append((a,d))
                set2 = set(new_relation)
                if b == c and ((a, d) not in self.cartesian_product()):
                    return False

        return True

    #We check that the relationship is reflexive
    #A relation is called reflexive when:
    #∀ a ∈ B, (a,a) ∈ cartesian product
    def reflexive(self):
        C = list(self.cartesian_product()) #List with cartesian product
        B = set(a for a, _ in C) #Browse the list
        result = set(ab for ab in C if ab[0] == ab[1])
        if len(B) == len(result): #Check if the length is equal
            return True
        else:
            return False


    #We check that the relationship is symetric
    # A relation is called symetric when:
    # ∀ (a, b) ∈ cartesian produc, (b, a) ∈ cartesian product
    def symetric(self):
        for set in self.cartesian_product():
            if set[::-1] not in self.cartesian_product(): #Function sset looking for the pair in crowd it reverses it and after loking it in cartesian product
                return False
        return True

    # equivalence classes divide into partition
    def equivalence_classes(self):
        h = int(input("Partiti:")) #We introduce from the keyboard in how many parts we want to share
        def rel(x1, x2):
            return int(x1) % h == int(x2) % h
        echivclass = [] #Found partitions
        for x in self.a:  #Loop over each element
            for echi in echivclass:
                if rel(x, echi[0]): #Found a partition for it!
                    echi.append(x)
                    break
            else:
                echivclass.append([x]) #Make a new partition for it
        return echivclass

    # if in the original list we have two tuples form (a,b) and (c,d) ,and b equals c ,then we add tuple (a,d).
    def transient_closure(self):
        global set2 #we use global variable
        inchidere = set(self.cartesian_product())
        ok = 1
        while ok == 1: #the loop will go until the variable ok gets 0
            multime2 = inchidere.union(set2)
            if multime2 == inchidere:
                ok = 0
                break
            inchidere = pereche_formata
        return inchidere


#Menu
k = -1
while k != 0:
  k = int(input("""
1.Inserare
2.Produs Cartezian
3.Verificare relatie echivalenta
4.Clase de echivalenta
5.Inchidere Tranzitiva
6.EXIT
Alegeti o optine:"""))
  if k == 1:
      M = myList()
      X = M.newList() #we make the list
      print (X)  #print the list
  elif k == 2:
    p = M.cartesian_product() #we make the cartesian product
    print (p) #print the cartesian product

  elif k == 3:
    # If is reflexive,tranzitive and symetric it results that the relationship is binary, to the contrary result "Relatia nu este echivalenta"
    t = M.tranzitive() #Check to see if it's transitive
    r = M.reflexive() #Check to see if it's reflexive
    s = M.symetric() #Check to see if it's simetric
    if t and r and s:
      print("Relatia este tranzitiva")
      print("Relatia este reflexiva")
      print("Relatia este simetrica")
      print("Relatia este echivalenta")
    else:
      print("Relatia nu este echivalenta")
  elif k == 4:

      claseEchiv=[] #An empty list where we will put the equivalence classes
      claseEchiv = M.equivalence_classes() #We display the equivalence classes
      print(claseEchiv)
  elif k == 5:
      t = M.tranzitive()
      inchidereTranz = M.transient_closure() #To show transiet closure first we had to show it was transitive
      print(inchidereTranz)
  elif k == 6 : #If you press keyboard "6" the menu will close
     break