import glob
import subprocess 
import os

class datamovement(object):
              
     def __init__(self):
         self.datapath=input("Enter the folder path for which you want to seggregate:")

     def extensiongetter(self):
                   distinctextenstions=[i.split(".")[-1]  for i in glob.glob("%s/*"%self.datapath) if ((len(i.split(".")[-1])>0) and ( "." in i))]
                   return list(set(distinctextenstions))

     def filemover(self):
             extensions=self.extensiongetter()
             print("extensions",extensions)
             for i in extensions:
                           status,output=subprocess.getstatusoutput("mkdir -p %s/%s"%(self.datapath,i))
                           if status!=0:
                                 print("Not able to make directory for following extension %s with following error %s"%(i,output))
                           else:
                               print("i",i)
                               filenames=[k for k in glob.glob("%s/*.%s"%(self.datapath,i))]
                               print("filenames",filenames)
                               for y in filenames:
                                           status,output=subprocess.getstatusoutput('mv "%s" %s/%s/'%(y,self.datapath,i))
                                           if status!=0:
                                                 print("unable to move the following file %s with error %s"%(y,output))
                                           else:
                                                 print("following file %s moved successfully"%y) 
                                                   
                                
                              
                                  
if __name__=="__main__":
                          t1=datamovement()
                          t1.filemover()

    
