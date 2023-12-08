import os
import json

directory = f'Day {input("What day is it: ")}'

parent_dir = json.load(open('prep.json'))['parent']

path = os.path.join(parent_dir, directory)

star1 = os.path.join(path, 'star1')
star2 = os.path.join(path, 'star2')

os.mkdir(path)
os.mkdir(star1)
os.mkdir(star2)