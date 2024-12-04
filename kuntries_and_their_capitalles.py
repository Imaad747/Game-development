"""kuntries={"USA":"Washington D.C",
          "UK":"London",
          "Russia":"Moscow",
          "China":"Beijing",
          "Australia":"Canberra",
          "France":"Paris",
          "Germany":"Berlin",
          "Pakistan":"Islamabad",
          "Egypt":"Cairo",
          "Saudi Arabia":"Riyadh",
          "Turkey":"Istanbul",
          "India":"New Delhi",
          "Nigeria":"Lagos",
          "Serbia":"Belgrade",
          "Italy":"Rome",
          "Japan":"Tokyo",
          "Poland":"Warsaw",
          "Afghanistan":"Kabul",
          "Netherlands":"Amsterdam",
          "Vietnam":"Ho Chi Minh City"}
print(kuntries["Poland"])
kuntries["Mexico"]="Mexico City"
print(kuntries)
print(kuntries.keys())
print(kuntries.values())

#nested dictionaries
claasrom={"Bob":{"Grade":82,"Marks":[12,2,60,99,1,3,4]},
          "Oof":{"Grade":-3,"Marks":[99,99,99,99,99,99,99]}}
print(claasrom["Oof"]["Marks"])


#voooowel finder
uiy=input("Enter a sentence for the vooowel.")
vowels={"a":0,
       "e":0,
       "i":0,
       "o":0,
       "u":0}
for item in uiy:
    if item in vowels:
        vowels[item]+=1
print(vowels)"""


#creating a panogram program
a={}
import string
for i in string.ascii_lowercase:
    a[i]=0
print(a)
stoprudderinput=input("Enter or type in a sentence.")
for iteem in stoprudderinput:
    if iteem in a:
        a[iteem]+=1
print(a)
check=True
for i in a.values():
    if i==0:
        check=False
if check==True:
    print("It is a panagram.")
else:
    print("It is not a panagram")