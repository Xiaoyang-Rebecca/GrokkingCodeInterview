#%%
import numpy as np 
import pandas as  pd 

df = pd.DataFrame ( {"x":[0,0,1,1],
      "y":[1,0,1,0],
      "p":[0.2,0.3,0.4,0.2],
      })

#!) mean

a = df.groupby("x").mean()
print (a)

# %%
