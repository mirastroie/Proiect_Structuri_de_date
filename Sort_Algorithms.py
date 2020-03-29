import timeit
import random


f=open("Inputs.in")
r=open("Outputs.out","w")


#Count Sort

# Count Sort este un algoritm de sortare pe care preferam sa il folosim in cazul sortarii numerelor intregi pozitive mici. In
# cel mai rau scenariu, complexitatea in functie de timpul de executie al algoritmului este O(n+MAX) unde n este numarul
# de elemente, iar MAX este cel mai mare numar din lista de elemente pe care vrem sa o sortam.
# Complexitatea in functie de  memoria utilizata este, de asemenea, O(n+MAX).


def count_sort(l):
    a=l.copy()
    if len(a)<=1:
        return a

    try:
        # Cream o lista de frecventa, in care vom retine de cate ori apar numerele de la 0 la maxim in lista pe care vrem
        # sa o sortam
        ma = max(a)
        nr=[0]*(ma+1)
    except MemoryError:
        r.write("Numerele sunt prea mari pentru count sort\n")
        return a

    except OverflowError:
        r.write("Numerele sunt prea mari pentru count sort\n")
        return a
    # Retinem pentru fiecare element din vector numarul de aparitii
    for x in a:
            nr[x]=nr[x]+1

    # Rescriem elementele din lista in ordine crescatoare, cu ajutorul listei de frecventa nr
    index=0
    for i in range(len(nr)):
                for j in range(nr[i]):
                    a[index]=i
                    index=index+1


    return a


#Insertion sort

# Insertion sort este un algoritm de sortare pe care preferam sa il folosim in cazul sortarii unui vector cu numar mic de elemente. Este
# o sortare:
#       in-place(nu foloseste structuri de date auxiliare)
#       stabila(pozitia relativa a elementelor egale din vector se pastreaza)
# Cel mai rau scenariu pentru un vector care vrem sa il sortam cu Insertion Sort este ca vectorul sau fie ordonat descrescator.
# Nu este eficient sa folosim Insertion Sort atunci cand vectorul este complet neordonat, cand avem un numar mare de elemente
# de sortat.

# Complexitatea in functie de timpul de executie: O(n^2)
# Bun de folosit cand toate elementele vectorului sunt deja sortate

def insertion_sort(l):
    b = l.copy()
    n=len(b)
    if n <= 1:
        return b
    for i in range(n):
        j=i-1
        k=b[i]
        while j>=0 and b[j]>k:
            b[j+1]=b[j]
            j=j-1
        b[j+1]=k
    return b


# Merge Sort si Quick Sort


# Merge Sort este un algoritm de sortare de tip divide et impera.  Este o sortare stabila.
# Complexitatea in functie de timpul de executie: O(nlogn)
# Complexitatea in functie de memoria utilizata: O(n)
# Presupune impartirea vectorului in 2 jumatati pana cand acesta nu mai poate fi impartit.

# Quick Sort
# Complexitatea in functie de timpul de executie, in cel mai rau scenariu: O(n^2)
# Complexitatea in functie de timpul de executie, pe cazuri normale: O(n*logn)
# Este un algoritm de sortare in-place.
# Presupune impartirea vectorului in 2 parti, nu neaparat jumatati.

#Codul pentru Merge Sort

def interclasare(l1,l2):

    i=0
    j=0
    rez=[]
    while(i<len(l1) and j<len(l2)):
        if l1[i]<l2[j]:
            rez.append(l1[i])
            i=i+1
        else:
            rez.append(l2[j])
            j = j + 1
    # La fiecare pas algoritmul separa lista actuala in 2 parti egale
    rez.extend(l1[i:len(l1)])
    rez.extend(l2[j:len(l2)])
    return rez

def merge_sort(l):
    if len(l)<=1:
        return l
    else:
        m=len(l)//2
        m1=merge_sort(l[0:m])
        m2=merge_sort(l[m:len(l)])
        return interclasare(m1,m2)

# Codul pentru Quicksort
# Implementarea folosind BFPRT - mediana medianelor

def swap(a,b):
    aux=a
    a=b
    b=aux

def mediana(A):
    if len(A)<=5:
        return sorted(A)[len(A)//2]
    subliste=[sorted(A[i:i+5]) for i in range(0,len(A),5)]
    mediane=[x[len(x)//2] for x in subliste]
    return mediana(mediane)

def pivot_partition(result,start,stop):
    median_pivot=result.index(mediana(result[start:stop+1]),start,stop+1)
    aux = result[median_pivot]
    result[median_pivot] = result[start]
    result[start] = aux
    return partition(result,start,stop)

def partition(result,start,stop):
    pivot = start # pivot
    i = start - 1
    j = stop + 1
    while True:
        while True:
            i = i + 1
            if result[i] >= result[pivot]:
                break
        while True:
            j = j - 1
            if result[j] <= result[pivot]:
                break
        if i >= j:
            return j

        aux = result[i]
        result[i] = result[j]
        result[j] = aux


def quick_sort(A,start,stop):

    if start<stop:
        partition_index=pivot_partition(A,start,stop)
        quick_sort(A,start,partition_index)
        quick_sort(A,partition_index+1,stop)

# Implementarea folosind mediana din 3

def mediana_din_3(result, start, stop):
    center=(start+stop)//2
    if result[center]<result[start]:
        swap(result[center],result[start])
    if result[start]<result[stop]:
        swap(result[start], result[stop])
    if result[stop]<result[center]:
        swap(result[center], result[stop])
    swap(result[center], result[start])
    return partition(result, start, stop)

def quick_sort_2(A,start,stop):

    if start<stop:
        partition_index=mediana_din_3(A,start,stop)
        quick_sort_2(A,start,partition_index)
        quick_sort_2(A,partition_index+1,stop)


# Radix Sort

# Complexitatea in functie de timpul de executie:  O((n+b) * logb(k)), unde b baza, iar k valoarea maxima
# Folosim Radix Sort cand: avem nevoie de un algoritm stabil
#                           avem de sortat multe numere
#                           numerele sunt foarte mari
# Urmatoarele implementari folosesc count sort ca subrutina

# Radix sort cu baza = 10
def counting(l,times):

      length=len(l)
      result=[0]*length
      count=[0]*(10)
      #retinem numarul de aparitii a fiecarei cifre luata ca cifra a zecilor, sutelor, miilor, etc.
      for x in l:
         cifra=(x//times)%10
         count[cifra]=count[cifra]+1

      for i in range(1,10):
          count[i]=count[i-1]+count[i]

      i=length-1  #luam de la coada la cap ca sa isi pastreze elementele egale ordinea din lista initiala
      while i>=0:
          cifra=(l[i]//times)%10
          result[count[cifra]-1]=l[i]
          count[cifra]=count[cifra]-1
          i=i-1
      for i in range(length):
          l[i]=result[i]

def radix_sort(l):
    result=l.copy()
    if len(result)<=1:
        return result

    ma=max(result)
    digit_position=1
    while ma/digit_position>0:
        counting(result,digit_position)
        digit_position=digit_position*10
    return result

# Radix sort cu baza = 16
# Mutatis Mutandis cu radix sort cu baza 10, cu observatia, pentru eficientizare, se folosesc operatii pe biti
def counting_2(a, shift):
   count=[0]*16
   n=len(l)
   result=[0]*n
   for x in a:
       count[(x>>shift) & 15]= count[(x>>shift) & 15]+1 #folosim shiftarea la dreapta si bit mask ca sa obtine o cifra hexadecimala
   for i in range(1,16):
       count[i]=count[i-1]+count[i]
   for i in range(n-1,-1,-1):
       index=(a[i]>>shift) & 15
       result[count[index]-1]=a[i]
       count[index]=count[index]-1
   for i in range(n):
       a[i]=result[i]


def radix_sort_2(l):
    b=l.copy()
    shift=0
    if len(l)<=1:
        return b
    ma=max(b)
    while (ma >> shift)>0: # <=> ma//(2**shift)>0
        counting_2(b, shift)
        shift=shift+4 #tinem cont ca orice cifra hexadecimala este 4 biti in binar
    return b

# Crearea unei functii care sa verifice daca un vector este sortat
def check_sort(result):
    for i in range(len(result)-1):
        if result[i]>result[i+1]:
            return False
    return True

# Generarea unei liste de N numere aleatorii cu valori pozitive mai mici decat MAX
def generate_numbers(N, MAX):
    l = []
    for i in range(N):
        l.append(random.randint(0, MAX))
    return l



T=int(f.readline()) #citirea lui T, numarul de teste

for i in range(T):

    print("For test nr.",i+1)
    # Citirea lui N si MAX pentru fiecare test
    line = f.readline()
    input=[int(x) for x in line.split()]
    N=input[0]
    MAX=input[1]
    # Apelam functia de generare a listei
    l=generate_numbers(N, MAX)
    r.write("Lista generata este="+str(l)+"\n")
    r.write("Test "+str(i+1)+" cu N="+str(N)+" si MAX="+str(MAX)+"\n")

    #Count sort
    start_time = timeit.default_timer()
    b=count_sort(l)
    finish_time=timeit.default_timer()
    r.write("Count sort time: "+str(finish_time-start_time)+"  Sort value:   "+str(check_sort(b))+"\n")
    print("Count is finished")

    #Insertion Sort
    if N<3000:
        start_time = timeit.default_timer()
        b = insertion_sort(l)
        finish_time = timeit.default_timer()
        r.write("Insertion sort time "+str(finish_time-start_time)+"  Sort value:   "+str(check_sort(b))+"\n")
        print("Insertion is finished")

    #Merge sort
    start_time = timeit.default_timer()
    b = merge_sort(l)
    finish_time = timeit.default_timer()
    r.write("Merge sort time: "+str(finish_time-start_time)+"  Sort Value:  "+str(check_sort(b))+"\n")
    print("Merge is finished")

    # Radix Sort
    #Radix sort cu baza 10
    if N<10000: # Din motive legate de timpul de asteptare a rularii programului si a performantei scazute
                # a variantei radix sort cu baza 10  pentru un vector de marime mare
        start_time = timeit.default_timer()
        b = radix_sort(l)
        finish_time = timeit.default_timer()
        r.write("Radix Sort - Base 10 time:" + str(finish_time - start_time) + "  Sort value:   " + str(check_sort(b)) +  "\n")
        print("Base 10 Radix is finished")

    #Radix sort cu baza 16
    start_time = timeit.default_timer()
    b = radix_sort_2(l)
    finish_time = timeit.default_timer()
    r.write("Radix sort - Base 16 time: " + str(finish_time - start_time) + "  Sort value:   " + str(check_sort(b)) +"\n")
    print("Base 16 Radix is finished")

    #Quick_sort - BFPRT
    start_time = timeit.default_timer()
    result = l.copy()
    quick_sort(result, 0, len(l) - 1)
    finish_time = timeit.default_timer()
    r.write("Quick sort - BFPRT Sort time: "+str(finish_time - start_time) + "  Sort value:   " + str(check_sort(result)) + "\n")
    print("Quicksort - BFPRT is finished")

    # Quick_sort - mediana din 3
    start_time = timeit.default_timer()
    result2 = l.copy()
    quick_sort_2(result2, 0, len(l) - 1)
    finish_time = timeit.default_timer()
    r.write("Quick sort - median of 3 time: " + str(finish_time - start_time) + "  Sort value:   " + str(check_sort(result2)) +"\n")
    print("Quicksort - median of 3 is finished")

    #Python sort
    start_time = timeit.default_timer()
    result3=l.copy()
    b=sorted(result3)
    finish_time = timeit.default_timer()
    r.write("Python Sort  time: " + str(finish_time - start_time) + "  Sort value:   " + str( check_sort(b)) + "\n")
    print("Python Sort is finished")

    r.write("\n\n")


    # Concluzie:  Datele obtinute in testele anterioare consolideaza ideea de la care am pornit: nu putem sa vorbim cu adevarat
    # despre "cel mai bun" algoritm de sortat in mod general. Alegerea unui algoritm se face pe baza restrictiilor datelor de intrare.
    # Astfel, este de preferat sa utilizam Count sort cand avem numere apropiate ca valoare, numere mici intregi pozitive. Este de
    # preferat sa utilizam Insertion Sort atunci cand vectorul pe care vrem sa il sortam este de marime mica si/sau cand deja avem o parte
    # din vector sortata. Putem sa folosim Merge Sort atunci cand nu stim restrictiile datelor de intrare. Putem folosi Quick sort
    # atunci cand average-case-urile de performanta conteaza mai mult decat worst-case-urile.


    # References: https://medium.com/karuna-sehgal/a-quick-explanation-of-quick-sort-7d8e2563629b
    # https://www.geeksforgeeks.org/  https://stackoverflow.com/
    # https://stackoverflow.com/questions/40350577/radix-sort-base-16-hexadecimals
    # Introduction to algorithms / Thomas H.Cormen[et al.].—2nd ed., 2002, The MIT Press, pages: 145-182