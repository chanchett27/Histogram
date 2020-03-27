import matplotlib.pyplot as plt

count = list(range(0,36))
chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

file = open("Syllabus_CIS298_001MannW20.txt")
text = file.read()
text = text.lower()

for i in range(0,36):
    count[i] = text.count(chars[i])

plt.plot(chars, count)
plt.title("Number of times each character occurs within the syllabus")
plt.ylabel("Number of occurrences")
plt.xlabel("Character")
plt.show()