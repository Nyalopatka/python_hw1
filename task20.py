scrabble = {1:"AEIOULNSTRАВЕИНОРСТ",2:"DGДКЛМПУ",3:"BCMБГЁЬЯ",
             4:"FHVWYЙЫ", 5:"KЖЗХЦЧ", 8:"JXШЭЮ", 10:"QZФЩЪ"  }

word = input("введите слово: ")
word = word.upper()

count = 0
for i in word:
    for key,value in scrabble.items():
        if i in value:
            count+=key
print(count)

