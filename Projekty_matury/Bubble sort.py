def bubble_sort(tab):
   rn = range(0, len(tab) )
   for i in rn:
       for j in rn:
            if j!=i and tab[i]<tab[j]:
                tab[i], tab[j] = tab[j], tab[i]



tab = [1, 2, 325, 12 ,54, 12, 6 ,7]

bubble_sort(tab)

print(tab)
