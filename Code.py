# write your code here
import copy

def no_parantesis(s):
    ok=0
    negatie=0
    j=0
    formula=[]
    for i in range(len(s)):
        if s[i]=='(':
            ok+=1
            if s[j]=='-':
                negatie=1
        if s[i]==')':
            ok-=1
            if ok==0: 
                negatie=0
        if s[i]!='(' and s[i]!=')':
            if negatie==1:
                if s[i]=='-':
                    formula.append('+')
                if s[i]=="+" or s[i]=='(':
                    formula.append('-')
                if s[i]!='+' and s[i]!='-':
                    formula.append(s[i])
            else:
                formula.append(s[i])
        if s[i]!=' ':
            j=i
    redone=''.join(formula)
    return redone

def simple_sum_constroction(s):
    third_list=list(s.split())
    empty_list=[]
    j=-1
    for i in range(len(third_list)):
        if third_list[i-1]=='^' and i>0:
            if empty_list[j-1][0]<='9' and empty_list[j-1][0]>='0':
                if third_list[i][0]<='9' and third_list[i][0]>='0':
                    q=int(empty_list[j-1])**int(third_list[i])
                    empty_list.pop(j)
                    j-=1
                    empty_list.pop(j)
                    empty_list.append(str(q))
                else:
                    q=int(empty_list[j-1])**int(dictionary[third_list[i]])
                    empty_list.pop(j)
                    j-=1
                    empty_list.pop(j)
                    empty_list.append(str(q))
            else:
                if third_list[i][0]<='9' and third_list[i][0]>='0':
                    q=int(dictionary[empty_list[j-1]])**int(third_list[i])
                    empty_list.pop(j)
                    j-=1
                    empty_list.pop(j)
                    empty_list.append(str(q))
                else:
                    q=int(dictionary[empty_list[j-1]])**int(dictionary[third_list[i]])
                    empty_list.pop(j)
                    j-=1
                    empty_list.pop(j)
                    empty_list.append(str(q))
        else:
            j+=1
            empty_list.append(third_list[i])
    third_list=copy.deepcopy(empty_list)
    empty_list=copy.deepcopy([])
    j=-1
    for i in range(len(third_list)):
        if third_list[i-1]=='*' and i>0:
            p=1
            if empty_list[j-1][0]<='9' and empty_list[j-1][0]>='0':
                p*=int(empty_list[j-1])
            if third_list[i][0]<='9' and third_list[i][0]>='0':
                p*=int(third_list[i])
            if empty_list[j-1][0]<='z' and empty_list[j-1][0]>='a':
                p*=int(dictionary[empty_list[j-1]])
            if third_list[i][0]<='z' and third_list[i][0]>='a':
                p*=int(dictionary[third_list[i]])
            empty_list.pop(j)
            j-=1
            empty_list.pop(j)
            empty_list.append(str(p))
        elif third_list[i-1]=='/' and i>0:
            if empty_list[j-1][0]<='9' and empty_list[j-1][0]>='0':
                q=int(empty_list[j-1])
            else:
                q=int(dictionary[empty_list[j-1]])
            if third_list[i][0]<='9' and third_list[i][0]>='0':
                p=int(third_list[i])
            else:
                p=int(dictionary[third_list[i]])
            empty_list.pop(j)
            j-=1
            empty_list.pop(j)
            empty_list.append(str(int(q/p)))
        elif (third_list[i-1]!='*' and third_list[i-1]!='/') or i==0:
            j+=1
            empty_list.append(third_list[i])
    new_string=" ".join(empty_list)
    return new_string

def ceckc_variable(s):
    if len(s)>0:
        if s[0]=='/':
            return 0
        else:
            cartus=list(s.split())
            ok=0
            egal=0
            paranteze=0
            for j in cartus:
                ok=0
                for i in j:
                    if len(j)>1 and (i=='*' or i=='^' or i=='/'):
                        return 4
                    if i=='(':
                        paranteze+=1
                    if i==')':
                        paranteze-=1
                        if paranteze<0:
                            return 4
                    if i>='a' and i<='z':
                        if ok==0:
                            ok=2
                        if ok==1:
                            if egal==0:
                                ok=-1
                            else:
                                ok=-2
                    if i>='0' and i<='9':
                        if ok==2 :
                            if egal==0:
                                ok=-1
                            if egal==1:
                                ok=-2
                        if ok==0:
                            ok=1
                    if i=='=':
                        egal+=1
                        ok=0
                    if ok==-1 or ok==-2:
                        break
                    if egal>1:
                        ok=-2
                        break
                if ok==-1 or ok==-2:
                    break
                if egal>1:
                    ok=-2
                    break
            if paranteze!=0:
                return 4
            if ok<0:
                return ok
            else:
                return egal
    return 3
        
        

def validity(s):
    if s[0]=='/':
        return False
    second_list=list(map(str,s.split()))
    a=second_list.count('-')+second_list.count('+')
    if a<=len(second_list)-a and a+1>len(second_list)-a:
        return False
    else:
        if second_list[len(second_list)-1][len(second_list[len(second_list)-1])-1]=='-' or second_list[len(second_list)-1][len(second_list[len(second_list)-1])-1]=='+':
            return False
        for i in second_list:
            for j in i:
                if j>='a' and j<='z':
                    return False
    return True
    

def list_constraction(s):
    number_list=[]
    first_list=list(map(str,s.split()))
    pozitivity=1
    for i in range(len(first_list)):
        if i == 0:
            number_list.append(int(first_list[0]))
            if first_list[0][0]=='-':
                pozitivity=-1
        if first_list[i][0]<='9' and first_list[i]>'0' and i>0:
            number_list.append(pozitivity*int(first_list[i]))
            pozitivity=1
        else:
            for j in first_list[i]:
                if j=='-':
                    pozitivity*=-1
    return number_list
    
    

s=input()
dictionary={}
while s!="/exit":
    if ceckc_variable(s)==0:
        if len(s)>0:
            if s[0]=='/':
                if s=="/help":
                    print("The program calculates the sum of numbers")
                elif s[0]=='/':
                    print("Unknown command")
            elif validity(s)==True:
                s=no_parantesis(s)
                s=simple_sum_constroction(s)
                l=list_constraction(s)
                if len(l)>0:
                    print(sum(l))
            elif validity(s)==False:
                s=no_parantesis(s)
                s=simple_sum_constroction(s)
                l=list(s.split())
                ok=1
                suma=0
                pozitivity=1
                for i in range(len(l)):
                    if l[i][0]!="+" and l[i][0]!="-":
                        if l[i][0]>='0' and l[i][0]<='9':
                            if pozitivity==-1:
                                suma-=int(l[i])
                            else:
                                suma+=int(l[i])
                        elif l[i] in dictionary:
                            if pozitivity==-1:
                                suma-=int(dictionary[l[i]])
                            elif pozitivity==1:
                                suma+=int(dictionary[l[i]])
                        else:
                            ok=0
                            break
                    else:
                        pozitivity=1
                        for j in l[i]:
                            if j=='-':
                                pozitivity*=-1
                            
                if ok==1:
                    print(suma)
                else:
                    print("Unknown variable")
    elif ceckc_variable(s)==1:
        if len(s)>0:
            l=list(s.split("="))
            l[0]=l[0].replace(" ","")
            l[1]=l[1].replace(" ","")
            if l[1][0]>='0' and l[1][0]<='9':
                dictionary[l[0]]=l[1]
            else:
                if l[1] in dictionary:
                    dictionary[l[0]]=dictionary[l[1]]
                else:
                    print("Invalid assignment")
    elif ceckc_variable(s)==-1:
        print("Invalid identifier")
    elif ceckc_variable(s)==-2:
        print("Invalid assignment")
    elif ceckc_variable(s)==4:
        print("Invalid expression")
    s=input()
print("Bye!")
