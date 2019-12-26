import pandas as pd
dataset = pd.read_csv('spambase.data')
count=0;
from sklearn.model_selection import train_test_split
training_data, testing_data = train_test_split(dataset, test_size = 0.2,random_state=0)
td = training_data.values.tolist()
ts=testing_data.values.tolist()
h=[]
s=[]
k=0
while k<57:
      h.append([])
      s.append([])
      k=k+1
     
i=0   
leng=len(td)     
while i<leng:
     le=len(td[i])
     j=0
     if td[i][le-1]==0:
         
         while j<le-1:
             if not(td[i][j] in h[j]):
                 h[j].append(td[i][j])
             j=j+1
     else:
         while j<le-1:
             
             if not(td[i][j] in s[j]):
                 s[j].append(td[i][j])
             j=j+1
     i=i+1
    
f=0
true=0
false=0
leng=len(ts)  
while f<leng:
    
    length=len(ts[f])
    j=0
    count1=0
    while j<length-1:
        
        if ts[f][j] in s[j]:
            count1=count1+1
            j=j+1
        else:
            j=j+1
    if count1==length-1:
        if ts[f][len(ts[f])-1]!=1:
            false=false+1
        else:
            true=true+1
    else:
        j=0
        count3=0
        while j<length-1:
        
          if ts[f][j] in h[j]:
            count3=count3+1
            j=j+1
          else:
        
            j=j+1
        if count1>count3:
            if ts[f][len(ts[f])-1]==1:
                   true=true+1
            else:
                   false=false+1
        else:
            if ts[f][len(ts[f])-1]!=0:
                   false=false+1
            else:
                   true=true+1
    f=f+1
    
tot=true+false
accuracy=float((true/tot)*100)  
print("accuracy percentage is",accuracy)

    
