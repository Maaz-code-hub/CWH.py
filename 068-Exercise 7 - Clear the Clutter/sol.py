import os 
l=os.listdir(".")
i=1
for item in l:
    if item.endswith(".png"):
        os.rename(item,f"{i}.png")
        i+=1
