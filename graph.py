import json
import matplotlib.pyplot as plt
from numpy import nan

file_path = 'hyperfine.json'

# Read and parse JSON data
with open(file_path, 'r') as file:
    data = json.load(file)

# Extracting data from the JSON structure
commands = data['results']
labels = [cmd['command'].split()[0] for cmd in commands]
means = [cmd['mean'] for cmd in commands]
stddevs = [cmd['stddev'] or nan for cmd in commands]
mins = [cmd['min'] for cmd in commands]
maxs = [cmd['max'] for cmd in commands]
# Creating the plot
fig, ax = plt.subplots()

# Bar chart for mean times with labeled exact seconds
bars = ax.bar(labels, means, yerr=stddevs, capsize=5, color='skyblue', label='Mean ± σ')

# Adding labels to the bars
for bar, mean in zip(bars, means):
    yval = bar.get_height()
    ax.text(bar.get_x() + (bar.get_width()/3) * 2, yval, round(mean, 2), va='bottom')

# Bar chart for mean times
ax.bar(labels, means, yerr=stddevs, capsize=5, color='gold', label='Mean ± σ')
ax.scatter(labels, mins, color='green', label='Min Time')
ax.scatter(labels, maxs, color='red', label='Max Time')

# Adding labels and title
ax.set_xlabel('Command')
ax.set_ylabel('Time in seconds')
ax.set_title('Comparison of Environment Creation Times')
ax.legend()

# Showing the plot
plt.savefig('hyperfine.png')
