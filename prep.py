import os
import json

#make paths
directory = f'Day {input("What day is it: ")}'
parent_dir = json.load(open('prep.json'))['parent']
path = os.path.join(parent_dir, directory)

print(path)
star1 = os.path.join(path, 'star1')
star2 = os.path.join(path, 'star2')
os.mkdir(path)
os.mkdir(star1)
os.mkdir(star2)

#add test data
file = open(f'{path}\\testinput.txt', 'w')
file.close()
file = open(f'{path}\\realinput.txt', 'w')
file.close()
input('Press enter after adding data')

testInput = open(f'{path}\\testinput.txt', 'r').read()
open(f'{star1}\\testinput.txt', 'w').write(testInput)
open(f'{star2}\\testinput.txt', 'w').write(testInput)
realInput = open(f'{path}\\realinput.txt', 'r').read()
open(f'{star1}\\realinput.txt', 'w').write(realInput)
open(f'{star2}\\realinput.txt', 'w').write(realInput)
os.remove(f'{path}\\testinput.txt')
os.remove(f'{path}\\realinput.txt')