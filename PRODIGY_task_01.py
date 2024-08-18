import pandas as pd
import matplotlib.pyplot as plt
file_path = 'worldpopulation.csv'  
data = pd.read_csv(file_path)
year = '2022'
filtered_data = data[['Country Name', year]].dropna()
plt.figure(figsize=(14, 8))
bars = plt.bar(filtered_data['Country Name'], filtered_data[year])
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:,.0f}', ha='center', va='bottom')

plt.title(f'Population Distribution Across Countries in {year}')
plt.xlabel('Country')
plt.ylabel(f'Population in {year}')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
plt.savefig('chart.png')
