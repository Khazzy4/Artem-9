
number_of_cats = 100
cats_with_hats = []
number_of_laps = 100
cats_with_hats_1 = []

# for cat_1 in range(1, number_of_cats + 1):
#     cats_with_hats.append(cat_1)


# for cat_2 in range(1, number_of_cats + 1):
#     if cat_2 % 2 == 0: 
#         cats_with_hats_1.append(cat_2)
# print(cats_with_hats_1)



# for cat_3 in range(1, number_of_cats + 1):
#     if cat_3 % 3 == 0: 
#         cats_with_hats.append(cat_3)
# print(cats_with_hats)



for cat in range(1, number_of_cats + 1):
    for lap in range(1, number_of_cats + 1):


        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)



print(cats_with_hats)