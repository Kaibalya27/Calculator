from tkinter import *

def number(i):
    global res
    if (res!=None):
        res=None
        clear()
    cur=result['text']
    if cur=='' and i==0:
        result['text']='0'
        return
    if (cur=='' or cur=='0') and i=='.':
        result['text']='0.'
        return
    if cur=='0':
        result['text']=str(i)
        return
    if i=='-':
        if cur=='':
            return
        if cur[0]=='-':
            result['text']=cur[1:]
        else:
            result['text']='-'+cur
    else:
        new=cur+str(i)
        result['text']=new

def operator(s):
    global first,op,res
    res=None
    first=result['text']
    if first=='':
        return
    op=s
    result['text']=''
    prev['text']=first+op

def clear():
    global first,last,op
    result['text']=''
    prev['text']=''
    first=last=op=None

def remove():
    result['text']=result['text'][:-1]

def results():
    global first,last,op,res
    last=result['text']
    if last=='0.':
        last='0'
    if (first=='') or (last==''):
        result['text']=(first or last)
        return
    prev['text']+=last
    if ('.' in first) or('.' in last):
        first=float(first)
        last=float(last)
    else:
        first=int(first)
        last=int(last)
    if op=='+':
        res=str(first+last)
    elif op=='-':
        res=str(first-last)
    elif op=='*':
        res=str(first*last)
    elif op=='^':
        res=str(pow(first,last))
    elif op=='/':
        if (last==0):
            res='Error'
        else:
            if(first%last==0):
                res=str(first//last)
            else:
                res=f'{float(first/last):.10f}'
    result['text']=res
    first=last=op=None


first=last=op=res=None
r=Tk()
r.title("Calculator")
r.geometry("300x458")

prev=Label(text='',fg='#36454F')
prev.config(font=(None,18))
prev.grid(row=0,column=0,columnspan=10,pady=(10,10),sticky='e')

result=Label(text='')
result.config(font=(None,24))
result.grid(row=1,column=0,columnspan=10,pady=(10,14),sticky='w')

cross=Button(text='<--',bg='black',fg='white',width=8,height=3,command=remove)
cross.config(font=('Helvetica',11,'bold'))
cross.grid(row=2,column=3)

point=Button(text='.',bg='black',fg='white',width=7,height=3,command=lambda x='.':number(x))
point.config(font=('Helvetica',11,'bold'))
point.grid(row=2,column=2)

power=Button(text='^',bg='black',fg='white',width=7,height=3,command=lambda x='^':operator(x))
power.config(font=('Helvetica',11,'bold'))
power.grid(row=2,column=1)

sign=Button(text='+/-',bg='black',fg='white',width=7,height=3,command=lambda x='-':number(x))
sign.config(font=('Helvetica',11,'bold'))
sign.grid(row=2,column=0)

for i in range(8,-1,-1):
    n=i%3
    k=(8-i)//3
    num=Button(text=i+1,bg='black',fg='white',width=7,height=3,command=lambda x=i+1:number(x))
    num.config(font=('Helvetica',11,'bold'))
    num.grid(row=k+3,column=n)
L=['+','-','*','/']
for i in range(4):
    sign=Button(text=L[i],bg='black',fg='white',width=8,height=3,command=lambda x=L[i]:operator(x))
    sign.config(font=('Helvetica',11,'bold'))
    sign.grid(row=i+3,column=3)
equal=Button(text='=',bg='black',fg='white',width=7,height=3,command=results)
equal.config(font=('Helvetica',11,'bold'))
equal.grid(row=6,column=2)

num0=Button(text=0,bg='black',fg='white',width=7,height=3,command=lambda x=0:number(x))
num0.config(font=('Helvetica',11,'bold'))
num0.grid(row=6,column=1)

c=Button(text='C',bg='black',fg='white',width=7,height=3,command=clear)
c.config(font=('Helvetica',11,'bold'))
c.grid(row=6,column=0)

r.mainloop()