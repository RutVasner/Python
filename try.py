def rectangle(hight, width):
    if hight == width or hight - width <= -5 or hight - width >= 5:
        print("המלבן  שטחו" , hight*width)
    else:
        print("המלבן  הקפו " , hight* 2 + width*2)
        
def oddNum(width):   # פונקציה שמחזירה את מספר האפשרויות לחזרה במגדל
    flag = 0
    for num in range(width, 0, -2):
            flag +=1
    return flag-2
     
def triangular(hight, width):
    opption = 4
    index = 0
    while opption >= 3:
        opption = int(input("welcome, you chosse triangular, please choose 1 for calculation and 2 for printing"))
    if(opption == 1):
        print("the scope is : " , hight*2 + width)
    else:
        if width%2 == 0 or width > hight * 2:
            print("Sorry we can'nt print your rectangle")
        else:
            linesNum = oddNum(width) #מספר החזרות בכל סט כוכבים
            print(linesNum , "linesnum")
            starsnum  = width       # מספר הכוכבים בכל שורה
            for starsnum in range(1, width+1, 2): #לולאה שעוברת על המגדל ומדפיסה את הכוכבים
                if starsnum == width or starsnum == 1:
                    print(int((width - starsnum) / 2) * " " , "*" * starsnum )
                elif starsnum == 3:
                    while index < ((int((hight-2) /(linesNum))) + int(((hight-2) % (linesNum)))):
                        print(int((width - starsnum)/2) * " ",starsnum * "*" )
                        index += 1
                    index = 0
                else:
                    while index < int((hight-2) / (linesNum)):
                        print(int(((width - starsnum)/2)) * " ",starsnum * "*")
                        index+=1
                    index = 0

    # print("tria - - hight  ", hight , "  width   " , width)

def main():
    hight = 0
    width = 0
    shape = 4
    while shape >= 4:
        shape = int(input("press 1 for rec , 2 for tria or 3 for exit"))
    while shape != 3:
        while hight < 2:
            hight = int(input("please enter the tower's hight"))
        width = int(input("please enter the tower's width"))
        if (shape == 1):
            rectangle(hight , width)
        if (shape == 2):
            triangular(hight , width)
        hight = 0
        width = 0
        shape = int(input("press 1 for rec , 2 for tria or 3 for exit"))
    


if __name__ == "__main__":
    main()
