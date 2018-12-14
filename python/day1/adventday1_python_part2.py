import itertools as it

f= open('adventday1_input')

current_freq=0
set_freq={current_freq}

for i in it.cycle(f.read().split("\n")[:-1]):
	if i[0]=='+':
		current_freq+=int(i[1:])
	if i[0]=='-':
		current_freq-=int(i[1:])
	if current_freq in set_freq:
		break
	else:
		set_freq.add(current_freq)

print (current_freq)