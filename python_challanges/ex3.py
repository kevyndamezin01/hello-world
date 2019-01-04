a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def check_num():
    if a < 5:
	    print(a)

check_num()
print(a)

num = raw_input("Choose a number: ")

new_list = []

for i in a:
	if i < num:
		new_list.append(num)

print(new_list)
