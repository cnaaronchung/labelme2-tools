# labelme2-tools
a tools for labelme

after use the labelme,and you will get more folders like XX_json,and in thess folds ,you will see four files:img.png,label.png,label_names.txt and label_viz.png.

however ,some modules like U-net only need two files like img.png and label.png, there are many files with same name,
so ,i write a python script to solve this problem,

DEMO

from ccim import *
cctoimage('./labels-json/',2,'./images/','./labels/');

cctoimage            #function' name
'./labels-json/',    #root path
2,                   #type of list
'./images/',         #images folder
'./labels/'          #labels folder

afer run this script,it will make the dir(images and labels) automatically.
![Dis](https://github.com/cnaaronchung/labelme2-tools/blob/master/QQ%E6%88%AA%E5%9B%BE20200311180531.png)
