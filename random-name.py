import random

# family = ["Mother", "Father", "Aunt", "Uncle", "Brother", "Sister" ]
# pairs = {}

# for p in range(len(family) // 2):
#     pairs[p+1] = ( family.pop(random.randrange(len(family))),
#         family.pop(random.randrange(len(family))) )

# print(pairs)


students =["Rāhula", "Visuddha", "Richard", "Upekkhā", "Vimutta", "Santi", "Dhammasudassī", "Pāla", "Paññā", "Upāli"]
pairs = {}

for p in range(len(students) // 2):
    pairs[p+1] = ( students.pop(random.randrange(len(students))),
        students.pop(random.randrange(len(students))) )

print(pairs)


# 2 class {1: ('Dhammasudassī', 'Upekkhā'), 2: ('Vimutta', 'Visuddha'), 3: ('Rāhula', 'Richard'), 4: ('Pāla', 'Santi'), 5: ('Upāli', 'Paññā')}


# 3 class {1: ('Richard', 'Rāhula'), 2: ('Pāla', 'Vimutta'), 3: ('Upāli', 'Dhammasudassī'), 4: ('Upekkhā', 'Paññā'), 5: ('Visuddha', 'Santi')}