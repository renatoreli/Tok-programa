#%%
a=7
if a%7==0:
    print("A je djeljiv sa 7")
else:
    print("A nije djeljiv sa 7")
#%%

#2
a=int(input())
if a<0:
    print("broj je negativan")
elif a>0:
    print("broj je pozitivan")
#%%

#3
a=int(input())
b=int(input())
zbroj = a+b
if zbroj > 20:
    print("Suma je veća od 20")
elif zbroj<20 :
    print("Suma je manja od 20")
#%%

#4
a=5
b=6
zbroj =a+b
umnozak=a*b
if zbroj==umnozak:
    print("umnozak i zbroj dva broja su jednaki")
else:
    print("Umnozak dva broja su razliciti")
#%%

#5
a=int(input())
b=int(input())

if b==a:
    print(a**2)
else:
    print(a*b)
#%%

#%%
#6
a="Renato"
if "a"  in a:
    print("Samoglasnik se nalazi u zadanoj rijeci")
else:
    print("nema samoglasnika")
#%%

#7
#%%
a=int(input())
if a==1:
    print(a+1)
else:
    print(a*5)
#%%

#8
#%%
a=int(input())
b=int(input())
if a ==True:
    print("True")
elif b==False:
    print("False")
elif a==False:
    print("False")
#%%

#9
#%%
a=int(input())
b=int(input())
if a>0 and b<a:
    print("True")
else:
    print("False")
#%%

#10
#%%
a=int(input())
b=int(input())
if a>0 and b<a:
    print("True")
elif a>b or b>0:
    print("True")
else:
    print("False")
#%%

#11
#%%
#%%
should_multiply = input("Zelite mi mnoziti?") =="da"
if should_multiply:
    a=int(input())
    b=int(input())
    print("Umnozak je", a*b)
#%%

#%%
#12
#%%
a=int(input("Unesite prvu stranicu"))
b=int(input("Unesite drugu stranicu"))
c=int(input("Unesite trecu stranicu"))
print(a,b,c)
if a!=b and a!=c and b!=c:
    print("trokut je raznostranican")
elif a==b and a==c and b==c:
    print("trokut je jednakostranican")
elif a!=b and b==c:
    print("trokut je jednakokracan")
else:
    print("trokut ne postoji")
#%%
#%%
#13
a=int(input("Unesi broj"))
if a>0:
    print("broj je pozitivan")
elif a==0:
    print("broj je nula")
elif a<0:
    print("broj je negativan")
#%%

#%%
#14
a=int(input("Unesi prvi broj"))
b=int(input("Unesi drugi broj"))
operation=input("unesi operaciju")
if operation =="*":
    print("Umnozak",a*b)
elif operation =="/":
    print("Kolicnik",a/b)
elif operation =="+":
    print("Zbroj",a+b)
elif operation =="-":
    print("Razlika", a-b)
#%%
#%%
#15
#%%
a=int(input("Unesi broj bodova od 1-100"))
if a<50:
    print("Ocjena nedovoljan")
elif a>50 and a<60:
    print("Ocjena dovoljan")
elif a>60 and a<70:
    print("Ocjena dobar")
elif a>70 and a<80:
    print("Ocjena vrlo dobar")
elif a >80:
    print("Ocjena odlican")

#%%



# %%
