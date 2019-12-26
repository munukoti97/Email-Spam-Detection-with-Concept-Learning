# Email-Spam-Detection-with-Concept-Learning
I. INTIAL STEP    The first step that is done as a part of implementation is that divide the given data-frame into two parts 80%, 20% randomly. Where we used the divided 80% data as training data and the remaining 20% as test data.using method and     Some modules called import pandas as pd train_test_split(dataset, test_size = 0.2,random_state=0) 
 
II. FORMULATION OF HYPOTHESIS  Firstly we created a hypothesis variable ‘l’ which is of the data type list. This hypothesis is appended only when the value of the last column in the training dataset is ‘1’that is spam in our case. l = [ [ ], [ ]] This hypothesis list ‘l’ contains 57 rows. Columns has no particular  number.

III. STEPS FOLLOWED IN IMPLEMENTATION 
Step1: The Then appended the values into the list while not considering the duplicate values.    if not (ds[i-1] [j] in l[j])                        l[j].append(da[i-1][j]) checks whether the data in the list or not if data is not there  in the list then new data will be added into the hypothesis aray  ds contains the data of the file.   
Step2:  Using the above hypothesis formed we test the 20% data by applying this hypothesis. 
 
Step3: Row in the test data list is compared with the hypothesis list. If the values match, then it passes to the next column. This process is repeated until all the data in the rows is read and compared. The data that matches is declared as spam and if one of the condition fails then we declare it as not-spam. Several if and else or nested if-else statements were used to implement the above. 
 
Step4:  To give an example, if the result of the comparison is given as spam but, the real data is not spam. In this type of condition, we increment the value of the variable False and if the value is correct the variable True is incremented.   Step5:  Then we calculate the accuracy by {[no. of values that are True/ no. of values that are (true and False)] *100}. 
 
 
