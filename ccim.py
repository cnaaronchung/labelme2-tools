import os,shutil
def cctoimage(path,types,images,labels):#type of list,2:all holds,;1:phase 1
    if not os.path.exists(images):
        os.makedirs(images)
        print('创建了iamge文件夹')
    if not os.path.exists(labels):
        print('创建了labels文件夹')
        os.makedirs(labels)
    if types==1:
        files=os.listdir(path)
        if len(files)==0:
            print('没有任务文件在这个目下录');
            exit();
        for item in files:
            print(item)
    else:
       for root,dirs,files in os.walk(path):
          for item in files:
             if item == 'img.png':
                 num=len(os.listdir(images))+1;
                 savename=num.__str__()+'.png'

                 sourpath=root+'/'+item ;
                 savepath=images+savename
                 shutil.copy(sourpath,savepath)

                 sourpath = root + '/label.png';
                 savepath = labels + savename
                 shutil.copy(sourpath, savepath)
                 print('处理完成1组....进行下一组')




