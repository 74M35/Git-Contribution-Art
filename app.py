import os

#A dictionary made of how many days ago it should write a certain amount of commits to github
daycol = {232:0, 231:9, 230:9, 229:9, 228:0, 227:0, 226:0, 225:9, 224:13, 223:13, 222:9, 221:9, 220:0, 219:0, 218:1, 217:13, 216:13, 215:9, 214:9, 213:9, 212:0, 211:0, 210:9, 209:9, 208:9, 207:9, 206:9, 205:1, 204:9, 203:9, 202:9, 201:9, 200:9, 199:1, 198:0, 197:1, 196:9, 195:9, 194:9, 193:1, 192:0, 191:0, 190:0, 189:1, 188:1, 187:1, 186:0, 185:0, 184:0}

#create a loop that will loop through from the first day to the last day
for i in range (232,184, -1):
    d = str(i) + " days ago"
    #create a loop that repeats for the amount of commits needed
    for x in range(0, daycol[i]):
        with open("file.txt", "a") as file:
            file.write(d + "\n")
            os.system("git add .")
            os.system("git commit --date='" + d + "' -m 'commit'")

os.system("git push")
