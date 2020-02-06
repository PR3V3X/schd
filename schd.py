import os
import bs4 as bs

# This removes html bloat from schd.html.
os.system("sed '1 , 277d; 494, 999d' <my_schd.html> schd_alt.html")

schd = open('schd_alt.html', 'r')

sauce = schd.read()
soup = bs.BeautifulSoup(sauce, 'html.parser')

# Searches for date, hours, and lunchs.
date = []
for div in soup.find_all('div', class_ = 'date'):
    date.append(div.text)

hours = []
for span in soup.find_all('span', class_ = 'hours'):
    hours.append(span.text)

lunch = []
for div in soup.find_all('div', class_ = 'bottom lunch'):
    lunch.append(div.text)

# Removes "\n" from list.
lunch = [x.replace('\n', '') for x in lunch]

schd.close()

print(f"{date}\n")
print(f"{hours}\n")
print(f"{lunch}\n")

file = open('data.txt', 'w+')

for i in date:
    file.write(i + '\n')

for i in hours:
    file.write('\n' + i)

for i in lunch:
    file.write('\n' + i)

file.close()

