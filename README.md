I could definitely improve this by making it work at any time instead of just this once. And could make the system to create the shape better instead of a massive dictionary

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| 13+ commits | ![#39d353](https://via.placeholder.com/10/39d353?text=+) #39d353|
| 9-12 commits | ![#26a641](https://via.placeholder.com/10/26a641?text=+) #26a641 |
| 5-8 commits | ![#006d32](https://via.placeholder.com/10/006d32?text=+) #006d32 |
| 1-5 commits | ![#0e4429](https://via.placeholder.com/10/0e4429?text=+) #0e4429 |

## Creating the heart
```python
daycol = {232:0, 231:9, 230:9, 229:9, 228:0, 227:0, 226:0, 225:9, 224:13, 223:13, 222:9, 221:9, 220:0, 219:0, 218:1, 217:13, 216:13, 215:9, 214:9, 213:9, 212:0, 211:0, 210:9, 209:9, 208:9, 207:9, 206:9, 205:1, 204:9, 203:9, 202:9, 201:9, 200:9, 199:1, 198:0, 197:1, 196:9, 195:9, 194:9, 193:1, 192:0, 191:0, 190:0, 189:1, 188:1, 187:1, 186:0, 185:0, 184:0}
```
In this dictionary in the <a href="https://github.com/74M35/Git-Contribution-Art/blob/main/heart.py">heart.py</a> heart.py file, each dictionary key is representitive of   
how many days ago to make the commit (from 25/10/2021 so this wont work on any other day).  
And the value pair is representitive of how many commits to make on that day to make it a  
certain shade of green (as shown by the above table)

## Commiting the heart
```python
for i in range (232,184, -1):
    d = str(i) + " days ago"
    for x in range(0, daycol[i]):
        with open("file.txt", "a") as file:
            file.write(d + "\n")
            os.system("git add .")
            os.system("git commit --date='" + d + "' -m 'commit'")
```

The first FOR loop will loop the amount of days from the first commit to the last, and the loop  
counts down from 232 as the commits need to start from the oldest date
```python
for i in range (232,184, -1):
```

The next FOR loop is to write the amount of commits for the colour the box needs to be
```python
for x in range(0, daycol[i]):
```
