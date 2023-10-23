''' This Program contain all function and information of list , In C/C++ it is referred as Array.
A List is an ordered collection of items and we can put any value of any data type in list.
Not like C++ , List is independent of Data Type and Size defining , In C++ we can store only elements of one data type in an array .
But In Python , List contain any element of any data type , "Even a List can contain a list/tuple in itself " . '''


Blank_List = []
print(f"\nBlank List shown by this : {Blank_List}")

List = [1,2,3,'Hello',2.5,True,[1,2,3]]

print(f"\nAn example of List : {List}")

'''Position of elements in List is called indexing . We can access elements of list by index value of element .
Indexing has two types Positive Indexing and Negative Indexing .'''

print("\nPositive and Negative Indexing of List : ")
print("\nList is          :",List)
print("\nPositive Indexing : 0  1  2     3      4     5       6")
print("\nNegative Indexing :-7 -6 -5    -4     -3    -2      -1")

co_ordinates = [[0,1],[10,10],[20,200]]
print(f"\nExample of List in a list is Co-Ordinates : {co_ordinates}")
print(f"\nAccessing elements of list in a list is as follows :  list_name[main_index_value][elements_index_value]")
print('\nFirts Elements : ',co_ordinates[0][0] ,"and",co_ordinates[0][1])

print("\nAccessing List Elements : ",List[0],List[1],List[5],List[6])

''' Modifying List Elements
'''
List[5] = "World"
print("\nReplaceing True with World and Modify List :" , List)
List[2]/=2
print("\nAt index position 2 element divided by 2 and store at index position  2 , modified List : ")
print(List)
print("\nWorld multiply by 10 and stroe at 5th position")
List[5]=List[5]*10
print(List)
List[5]= 'World'
print('\nModifying List ',List)


'''
            Adding Elements in a List by append(New_element_value) and insert(index_value , New_element_value) function.

            Append function used to add element in Last position of list.
            
            Insert function used to add element at any position in list and other element's position shift/changes accordingly.'''


print('\nPrinting List : ',List)
print('\n\n\nAdding 100 at last position of List')
List.append(100)
print(List)
print('\nInserting 200 at 3rd postion of List')
List.insert(3,200)
print(List)


''' Removing Elements from a List : -

        (I) del statement : -  used to delete a element from list by using index value.

                    Syntax : -
                                 del List_name[index_position]


        (II) pop() method : -  pop() method removes the last element from a list and return that element .
                               Can not be modified default is last element.

                   Syntax : -
                               Variable_Name = List_Name.pop()    # By default remove and return last postion value , cannot be changed.
                               

                               
        (III) remove() method : - remove() function takes element value not index position , this is main difference between del and remove function.

                  Syntax : -
                             List_Name.remove(Element_Value)    this function cannot be empty.

                             If element is repeated more than one than remove function delete only once and stop.

                             '''

print('\n\n\n\nDeleting 2nd Postion i.e. 1.5 from List : ')
del List[2]
print(List)
print('\nDeleting and returning by default last element i.e. 100 from List.')
Last_element = List.pop()
print(List)
print('\nRetured Element : ',Last_element)
print('\nDeleting particular element by value (not by index position) let 200')
List.remove(200)
print(List)


'''
    copy() function : copy function copy the list to another variable , if another variable cleared then original list remains unchanged.
    clear() function clear the whole list and covert to a blank list.
    If we direct assign value b = a like this , the if  b clear then a also will be automatic clear . That's why we use copy function to save and protect our data.
'''

Copy_List = List.copy()
print('\nOriginal List',List)
print('\nCopied List by copy() function. :',Copy_List)
Copy_List.clear()  # Clear copy list without interfering in original list.
print('\nClearing Copy list .',Copy_List)
print('\nOriginal List : ',List)

''' Copying list by = assign operator affect original list.that's why we use copy function to save original data.'''

a = [1,2,3,4]
print('\n\n a List :',a)


print('\nInserting "Hello" element in a between 1 & 2 , i.e. at index postion 2')
a.insert(2,"Hello")
print('\nNow Modified List a : ',a)


b = a  # a data is assign to b.
b.append(100)

print('\n\n after modifying list b , wnwanted modification in list a :',a)

print('\nmodified list b :',b)

b.clear()  # Clearing list b affect original list a . that's why copy function is safe for data.

print('\n We have not modified list a , Unwanted modification occurs automatically in a. \nPrinting a ',a,'Printing b :',b)



'''
    reverse() function reverse the order of list elements (opposite) . (Not in increasing/decreasing just reverse.)
    
    
    sort() function : sort function arrage list in increasing and decreasing order. In sort function reverse = False by default so it arrage list in increasing order.

                      If reverse = True then it will print list in decreasing order.

                      key arugument is used to sort tuple in increasing or decreasing order.

                      sort(key = None , reverse = False) by default function.
                      sort function can not sort integer and string values contain in single list.
                      while using sort function takes string and integer value in different lists.

                      
    len(List_Name)  :  count the total elements in the list.

    sorted() : It makes a copy of list after sorting , while in sort function store sort list in original list.
    
    count(element_value) function : count function count how many times a element repeat.
                                    count(element_value) and count element repeatation.
                                    

    index(element_value) function : index function finds at which index postion the element place.
                                    Argument in this function is element value not index position number.
                                    

    extend(List_name or elemnt_values... in list) function : extend function add two lists.
                                                             extend function not add direct values .
                                                             value must be in list form .
'''

print('\n\n\nList : ',List)
List.reverse()
print('\nPrinting list in reverse order :',List)


print('\nCreating New List of integer :')
New_List = [22,1,3,0,56,64,10,12,32,6,3,2]
            
New_List.sort()
print('\nSorting List in Increasing order : \n',New_List)

New_List.sort(reverse= True)
print('\nSorting List in decreasing order : \n',New_List)



String_List = ["Hello","World","Param","Sahu","Python","IDLE","Interpreter","List","Function"]

print('\n\n\nNew string list : \n',String_List)

String_List.sort()
print('\nSorting String List in Increasing order by ASCII value (Alphabatical order) : \n',String_List)

String_List.sort(reverse= True)
print('\nSorting String List in decreasing order by ASCII value (Alphabatical order): \n',String_List)

String_List = ["Hello","World","Param","Sahu","Python","IDLE","Interpreter","List","Function"]

Sub_List = sorted(String_List)
Sub_List2 = sorted(String_List,reverse = True)
print('\nSorting List in Increasing order by sorted function : \n',Sub_List)
print('\nSorting List in Decreasing order by sorted function : \n',Sub_List2)
print('\nOriginal List : \n',String_List)

print('\nTotal Lenth/Total elements of/in the String List : ',len(String_List))
print("\nFinding Index position of Param, Python and Sahu : ",String_List.index("Param"),String_List.index("Python"),String_List.index("Sahu"))
print("\n\n\nAdding Windows , Laptop and New in String List \n",String_List.extend(["Windows","Laptop","New"]))


List2 = [1,2,3,2,1,2,1,23,42,1,15.3,'Hello',1,2,4,23,3,10,5,4,7,8,10,1]

print('\n\n\nList 2:\n',List2)
print('\nCounting 1 , 2 ,3 ,23 ,10,15,4,5,7,8,9,42 in List :\n',List2.count(1),List2.count(2),List2.count(3),end = " ")
print(List2.count(4),List2.count(5),List2.count(23),List2.count(42),List2.count(7),List2.count(8),List2.count(9))



print("\n\n\nAdding String_List and List2 and storing in String List : \n")
String_List.extend(List2)
print("\nString List : \n",String_List)
print("\nList2 : ",List2)

print('\nPrinting List List2 by for Loop \n')

for element in List2 :
    print(element)

colors = ['Red','Blue','Green','Indigo']

red,blue,green,indigo = colors
print('\nList Unpacking: ',red,blue,green,indigo)

colors.extend(['Brown','White','Black'])
red,blue,green,indigo,*other_colors = colors
print('\n List Unpacking : ',red,blue,green,indigo)
print(other_colors)



''' Sorting tuples in a List '''

companies = [("Google",2019,234.22),("Meta",2019,231.22),("Apple",2019,343.22),("Microsoft",2019,232.22)]
print("\n\nComapanies are : \n",companies)

companies.sort(key = lambda company: company[2])
print("\nIncreasing order of networth of companies\n",companies)

companies.sort(key = lambda company: company[2],reverse = True)
print("\nDecreasing order of networth of companies\n",companies)




print('\n\ncolors list are :\n',colors)

colors[0:2]=["Black","White","Gray"]
print('\nReplaceing Red , Blue by slicing\n',colors)

print("\n\nElements to be deleted : ",colors[2:5])


print('\n\nOriginal List ',colors)


print("\n\n\nDeltitg Elements by slicing : ")

del colors[2:5]
print(colors)

print('\n\nfirst List :\n',List)
List.extend(colors)
List.extend(String_List)
print('\nModifing List : \n',List)

''' Slicing List by 3 steps '''
print("\n\nSlicing List by 3 steps till 25th element :\n ",List[0: 26: 3])


print('\nPrinting index and values of list by enumerate function : ')

for enum in enumerate(String_List):
    print(enum)

print('\nMap function with lambda function : ')
new_list = list(map(lambda var : var*3,List2))
print(new_list)

''' If you multiply a x number to a string then it wil print x times that string.'''
new_list.remove('HelloHelloHello')
print(new_list)

print('\nFilter function fiter elements greater than 20 :\n ')
filtered = list(filter(lambda value : value>20,new_list))
print('\nFiltered List  : \n')
print(filtered)


print('\n\nList comprehension : \n')
filtered = [m for m in new_list if m<50]
print(filtered)

''' List comprehension is a technique for creating and modifiying the list in shorter way .'''

print("\n odd Numbers  til 100 and 3 multiple's  squares : \n")
numbers = [num for num in range(100) if num%2!=0]
print(numbers,'\n')
squares = [n**2 for n in numbers if n%3==0]
print(squares)