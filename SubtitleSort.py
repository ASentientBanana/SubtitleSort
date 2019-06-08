import sys , os 


#function for deleting old files
print(dir(os.rename))
def delete():
    print('deafult is for subtitles .srt file')
    inp = input('please enter a file type or leave empty for defoult: ')
    d = os.listdir()
    for i in d:
        if inp == "":
            p =".srt"
        else:
            p = inp
        if p in i:
            os.remove(i)
        else:
            continue

#delete()
def TitleNames():
    titles = []
    videos = []
    misc = os.listdir()
    for i in misc:
        if '.srt' in i:
            titles.append(i)
        elif ".mkv" in i or ".flv" in i or ".avi" in i or ".mov" in i or ".mp4" in i or ".gif" in i or ".m4a" in i :
                   
            videos.append(i)        
             
    # ^^^^^^^^^^sorts sub files and video files(any other type than .srt)^^^^^^^^^^^
##  
    temp = []
    newNames = []
    for video in videos:
        x= list(video)
        x.reverse()
        print(x)
        n = 0
        for i in x:
            n += 1
            if i == ".":
                temp = x[n::]
                temp.reverse()
                break
        word = ''.join(temp)
        newNames.append(word+'.srt')
        temp.clear()
    #^^^^^^^^^^^^^takes ccare of the name changes in the logic (doesnt change them on the sistem)^^^^^^^^^^^
    count= 0
    for tName in titles:
        os.rename(tName,newNames[count])
        count += 1

    print(newNames)
        
            
            
print("just press enter for the  default action rename ")
inp = input("for Deleting files enter 'd'or 'D' and for renaming filesenter 'r' or 'R' ")

if inp.lower() == "r" or inp == "":
    TitleNames()
elif inp.lower() == "d":
    delete()


