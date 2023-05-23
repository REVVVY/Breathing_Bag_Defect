import json
import matplotlib.pyplot as plt

json_files = ['D1.json', 
              'D2.json',
              'D3.json']
training_data = []

for file in json_files:
    with open(file, 'r') as f:
        data = json.load(f)
        training_data.append(data)

x = [[] for _ in range(len(json_files))] 
y = [[] for _ in range(len(json_files))] 

for i, data in enumerate(training_data):
    for point in data:
        x[i].append(point[1])
        y[i].append(point[2])

plt.figure(figsize=(10, 6)) 

for i in range(len(json_files)):
    plt.plot(x[i], y[i], label=f'D{i+1}')

plt.title('Region Proposal Network bounding box validation loss over epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()