import os
import json
import re
from datetime import timezone
from datetime import datetime
import requests

#make paths
date = str(int(datetime.now(timezone.utc).strftime('%d')))
directory = f'Day {date}'
parent_dir = json.load(open('prep.json'))['parent']
path = os.path.join(parent_dir, directory)

star1 = os.path.join(path, 'star1')
star2 = os.path.join(path, 'star2')
os.mkdir(path)
os.mkdir(star1)
os.mkdir(star2)

#add test data
file = open(f'{path}\\testinput.txt', 'w')
file.close()
input('Press enter after adding data')

testInput = open(f'{path}\\testinput.txt', 'r').read()
open(f'{star1}\\testinput.txt', 'w').write(testInput)
open(f'{star2}\\testinput.txt', 'w').write(testInput)
realInput = requests.get(f'https://adventofcode.com/2023/day/{date}/input', cookies={'_ga': json.load(open('prep.json'))['cookies']}).text
#remove new line
realInput = realInput[:len(realInput)-1]
open(f'{star1}\\realinput.txt', 'w').write(realInput)
open(f'{star2}\\realinput.txt', 'w').write(realInput)
os.remove(f'{path}\\testinput.txt')

#copy python template
template = open('template.txt', 'r').read()

open(f'{star1}\\main.py', 'w').write(re.sub('DATE', date, re.sub('STAR', '1', template)))
open(f'{star2}\\main.py', 'w').write(re.sub('DATE', date, re.sub('STAR', '2', template)))