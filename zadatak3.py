#1
a=int(input())
b=int(input())

zbroj=a+b
print(zbroj)
razlika=a-b
print(razlika)
umnozak=a*b
print(umnozak)
kolicnik=a*b
print(kolicnik)
ostatak=a%b
print(ostatak)
potenciranje=a**2
print(potenciranje)
cjelobrojno=a//b
print(cjelobrojno)
#%%
#4
a=int(input("Unesite prvi broj"))
b=int(input("Unesite drugi broj"))
if a==b:
    print("jednako")
elif a>b:
    print("A je vece od B")
elif a>=b:
    print("A je vece ili jednako B")
# %%
#7 #8 #9 #10
#http://dontpad.com/lipik_ai_zadatci

a=5
b=10
c=15
d=21
sredina=(a+b+c+d)/4
print(sredina)
sredina2=int(sredina)
print(sredina2)
sredina3=sredina2*sredina2
print(sredina3)
rezultat=sredina3*100
print(rezultat)
# %%
#11
a=int(input("Unesi temperaturu u Celzijusu"))
f=(a*9/5)+32
print("Temperatura u Fahrenheitima je: ",f)

# %%
#12
a=int(input())
b=int(input())
zbroj=a+b
razlika=a-b
umnozak=a*b
kolicnik=a/b
print(a,"+",b,"=",zbroj)
print(a,"-",b,"=",razlika)
print(a,"*",b,"=",umnozak)
print(a,"/",b,"=",kolicnik)
# %%
#13

c=int(input("Unesite iznos"))
p=int(input("Unesite kamatu"))
m=int(input("Unesite broj mjeseci"))
k=c*p*m/2400
print(k)

# %%
#14
n=int(input("Unesi broj kuna"))
m=int(input("Unesi cijenu čokolade"))

b=n//m
print("Moze se kupiti",b,"čokoladi")

o=n%m
print("Ostalo je",o,"kuna")
# %%

#15
import math
a=int(input("Unesi prvu katetu"))
b=int(input("Unesi drugu katetu"))

c=(a**2+b**2)
c=math.sqrt(c)
print(c)
#%%
#16
a=int(input("Unesite prvi broj"))
b=int(input("Unesite drugi broj"))

zbroj=a+b
zbroj=float(zbroj)
print(zbroj)

# %%
#17
a=int(input("Unesite prvi broj"))
b=int(input("Unesite drugi broj"))

suma=a+b
razlika=a-b
umnozak=a*b
kolicnik=a//b
print(suma,razlika,umnozak,kolicnik)
# %%
#18

a=int(input("Unesite a"))
b=int(input("Unesite b"))
c=int(input("Unesite c"))

x= b**2-(4*a*c)

print(x)

# %%
#%%
#19
a=1
b=2
c=3
d=4
e=5
f=6
g=7
average=(a+b+c+d+e+f+g)/7
print(average)
#%%


#20

x=int(input("Unesi broj kuna"))
y=int(input("Unesi cijenu čokolade"))

print("Vlatka je dobila",x,"kuna")
print("Jedna cokoladica kosta",y,"kuna")

b=x//y
print("Moze se kupiti",b,"čokoladi")

o=x%y
print("Ostalo je",o,"kuna")
# %%
#21
broj_str=(input("Unesite dvoznamenkasti broj"))
broj1=int(broj_str[0])
broj2=int(broj_str[1])

print(broj1)
print(broj2)
# %%
#22
broj_str=(input("Unesite dvoznamenkasti broj"))
broj1=int(broj_str[0])
broj2=int(broj_str[1])

print(broj1+broj2)
# %%
#23
broj_str=(input("Unesite troznamenkasti broj"))
broj1=int(broj_str[0])
broj2=int(broj_str[1])
broj3=int(broj_str[2])
print(broj3,broj2,broj1)
# %%
#24

broj1_str=(input("Unesite prvi broj"))
broj2_str=(input("Unesite drugi broj"))
broj3_str=(input("Unesite treci broj"))
broj4_str=(input("Unesite cetvrti broj"))
broj5_str=(input("Unesite peti broj"))
broj6_str=(input("Unesite šesti broj"))
broj7_str=(input("Unesite sedmi broj"))
broj1=int(broj1_str[0:1])
broj2=int(broj2_str[0:1])
broj3=int(broj3_str[0:1])
broj4=int(broj4_str[0:1])
broj5=int(broj5_str[0:1])
print("Joker je",broj1,broj2,broj3,broj4,broj5)

# %%
