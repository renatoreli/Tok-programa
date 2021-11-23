#1
#%%
x="Dobar dan svima"
print(x)
#%%

#%%
#2
x="Dobar dan svima"
print(x[5:9])



#%%
#3
a="jedan dva tri "
b=" dva tri cetiri"
c=a+b
print(c)
print(a*3)
a=a.index("jedan")
print(a)



# %%

#%%
#4
a="    jedan    "
a= a.capitalize()
print(a)
a=a.lower()
print(a)
a=a.upper()
print(a)
a=a.title()
print(a)
a=a.lstrip()
print(a)
a=a.rstrip()
print(a)
a=a.strip()
print(a)

# %%
#5
a="venividivici"
print(len(a))
print(a[0:6])

# %%
#6
a="rijec"
print(a*5)
# %%
#7
a="rijec"
b="recenica"
print(a+b)
#%%
#8
a="abrakadabra"
a=a.replace("a","o")
print(a)

# %%
#10
broj_str=(input("Unesite troznamenkasti broj"))
broj1=int(broj_str[0])
broj2=int(broj_str[1])
broj3=int(broj_str[2])
print(broj1+broj2+broj3)


# %%
#11
broj_str=(input("Unesite troznamenkasti broj"))
broj1=int(broj_str[0])
broj2=int(broj_str[1])
broj3=int(broj_str[2])
print(broj2,broj1,broj3)


# %%

#%%
#12
x="stringing"
print(x[3:6])

# %%
#%%
#13
s1="random"
s2="nijerandom"

s1_first_half = s1[ :len(s1)//2]
s2_second_half = s2[ len(s2)//2:]

print(s1_first_half+s2_second_half)


# %%
#14

s1="random"
s2="nijerandom"
print(len(s1))
print(len(s2))


#%%
#16
x="Lipik"[::-1]
print(x)

# %%
