###############################
## EXERCISE: Test yourself by predicting what the output is and
##           what gets mutated then check with the Python Tutor
###############################
cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool)
print(warm)

colors1 = [cool]
print(colors1)
colors1.append(warm)
print('colors1 = ', colors1)

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']]
print('colors2 =', colors2)

warm.remove('red')
print('colors1 = ', colors1)
print('colors2 =', colors2)

for e in colors1:
    print('e =', e)

for e in colors1:
    if type(e) == list:
        for e1 in e:
            print(e1)
    else:
        print(e)

flat = cool + warm
print('flat =', flat)

print(flat.sort())
print('flat =', flat)

new_flat = sorted(flat, reverse = True)
print('flat =', flat)
print('new_flat =', new_flat)

cool[1] = 'black'
print(cool)
print(colors1)
