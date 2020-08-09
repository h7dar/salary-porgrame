#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import matplotlib.pyplot as plt


# In[34]:


employee_info1 = [('ID','f8') ,('names','S10') ,('increament','S32')]


# In[35]:


emplyees_staff1 = np.zeros((3), dtype = employee_info1)


# In[41]:


emplyees_staff1[0] = (1 , 'ali' , 0.08)
emplyees_staff1[1] = (2 , 'huda' , 0.10)
emplyees_staff1[2] = (3 , 'ahmed' , 0.5)


# In[46]:


employee_info2 = [('ID','f8') ,('work duration','S32') ,('salary','S32')]


# In[47]:


emplyees_staff2 = np.zeros((3), dtype = employee_info2)


# In[48]:


emplyees_staff2[0] = (1 , 3  , 2000)
emplyees_staff2[1] = (2 , 2  , 3500)
emplyees_staff2[1] = (3 , 6  , 2300)


# In[50]:


class empo:
    
    def name():
  
        name = emplyees_staff1['names']
        Id = emplyees_staff1['ID']
        increament=emplyees_staff1['increament']
        duration=emplyees_staff2['work duration']
        salary=emplyees_staff2['salary']
        
        
    def salary(self,name):
        x=input('Enter Name')
        if  (x==str('ali')):
            selali=((salary[0]*increament[0])*duration[0])
            alisalary=(salary[0]+selali)
            y = np.sin(alisalary)
            plt.title("Ali")
            plt.plot(alisalary, y)
            plt.show()
            print('Name:',name[0])
            print('Salary:',alisalary)
            
        elif(x==str('huda')):
            selhuda=((salary[1]*increament[1])*duration[1])
            hudasalary=(salary[1])
            y = np.sin(alisalary)
            plt.title("huda")
            plt.plot(hudasalary, y)
            plt.show()
            print('Name:',name[1])
            print('Salary:',hudasalary)
            
        elif (x==str('ahmed')):
            selahmed=((salary[2]*increament[2])*duration[2])
            ahmedsalary=(salary[2]+selahmed)
            y = np.sin(alisalary)
            plt.title("Ahmed")
            plt.plot(ahmedsalary, y)
            plt.show()
            print('Name:',name[2])
            print('Salary:',ahmedsalary)
       


# In[51]:


def main():
    empoly=empo()
    empoly.salary(name)
if __name__ == '__main__':main()


# 

# In[5]:





# In[ ]:




