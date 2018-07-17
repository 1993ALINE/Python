
# coding: utf-8

# In[8]:


from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()


# In[9]:


print(digits.data) 


# In[10]:


digits.target


# In[11]:


digits.images[0]

