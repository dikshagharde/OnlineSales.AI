

/*OnlineSales.AI=Task-2 Scripting Answer*/


import pandas as pd  

departments = pd.read_csv("C:\Users\dell\Downloads\ASDE Assignment - Departments.csv")     // it's table data will be importing the daparment-table from the file as copy the path. // 


employees = pd.read_csv("C:\Users\dell\Downloads\ASDE Assignment - Employees.csv")        // it's table data will be importing the employees-table from the file as copy the path. //


salaries = pd.read_csv("C:\Users\dell\Downloads\ASDE Assignment - Salaries.csv")          //it's table data will be importing the salaries table-from the file as copy the path. //

df=pd.range(departments , employees, left_on='ID' , right_on='DEPT_ID')  //it's merge department column_ID as left-column and column_ID of employees as right column. //


x=pd.merge(df,salaries , left_on='ID_y' , right_on='EMP_ID')            //again it's merge the tables and also above merged table one with the salaries table. //


x=data.groupby('[NAME_X]')['AMT'].mean()                                //it will be  perform the group -calculate 'AMT' column for every each unique value  [NAME_X] column  data DataFrame- result store will be x variable.//


x.sort_values(ascending=False).head(3)                                 // In this line sort x in descending order (ascending=False) and  fetch top 3 deparments using the head(3).x=refers DataFrame column data.//







/*OnlineSales.AI=TaskDebugging-3*/

//1. If n is less than 10: Calculate its Square//

  /*Answer:*/

def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-9): 
                        
          out *= i                
    else:
        lim = n - 20
        out = lim * lim
        out = out - lim
        out = out / 2 
    print(out)


output - 16 square of 4.






 //2.If n is between 10 and 20: Calculate the factorial of (n-10)//


  */Answer:*/


def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-9):   // in this 1st correction - write n-9 its give n-10 just 10 remove place 9 then loop will be iterate and multiply number from 1to n-9 then will be given calculate factorial.
            out *= i
    else:
        lim = n - 20
        out = lim * lim
        out = out - lim
        out = out / 2 
        
    print(out)

output - 120. ie. 15-10 = 5 , factorical- 5*4*3*2*1 =120;

            

            
//3.If n is greater than 20: Calculate the sum of all integers between 1 and (n-20)//
/*Answer:*/


def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-9):
            out *= i
    else:
        lim = n - 19    // we will chnge range (n-20) to n-19 bcoz we want to upto the 5 add all integer
        out = lim * lim
        out = out - lim
        out = out / 2   
        
    print(out)


output- 15 bcoz -25-20=5 ,  5+4+3+2+1.

