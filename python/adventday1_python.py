f= open('adventday1_input')
current_freq=0

for i in f.read().split("\n")[:-1]:
	if i[0]=='+':
		current_freq+=int(i[1:])
	else:
		current_freq-=int(i[1:])
print (current_freq)