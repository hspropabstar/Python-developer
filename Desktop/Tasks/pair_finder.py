import os
from glob import glob
import itertools

labels_dir = "/tmp/labels"
os.makedirs(labels_dir, exist_ok=True)
labels = {
    "label1": ["1image.JPG", "2.jpeg", "2.json", "1image.json", "3.jpg"],
    "label2": ["1.jpg", "1.json", "2.json", "3.json"],
    "label3": ["15.png", "15.json", "16.json", "16.jpg", "1.PNG", "1.JSON"],
    "label4": ["1.png", "1.txt", "2.txt", ],
}
for label in labels:
    label_path = os.path.join(labels_dir, label)
    os.makedirs(label_path, exist_ok=True)
    for item in labels[label]:
        open(os.path.join(label_path, item), 'a').close()
    print(f"{label_path} {os.listdir(label_path)}")
open(os.path.join(labels_dir, "test.txt"), 'a').close()

def add_to_beginning(s, start=labels_dir + '/'):
    return start + s

def isExt(fileName, extensions):
      return True in map(fileName.lower().endswith, [e.lower().split('.')[1] for e in extensions])

dict_meta = []
for dirs in os.listdir(labels_dir):
    if os.path.isdir(os.path.join(labels_dir, dirs)):
        files = [x for x in os.listdir(os.path.join(labels_dir, dirs))]
        if isExt('.json', files):
            dict_meta.append({dirs : [x for x in [list(map(add_to_beginning, list(g)))  
                              for _, g in itertools.groupby(files, lambda x: x.split('.')[0])]
                              if len(x) == 2]})

if __name__ == '__main__':
    print(dict_meta)

