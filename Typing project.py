from time import time

print('Instructions: ')
print('Press enter to start typing and press enter twice to stop typing')
input('Press enter to start typing: ')

start = time()
text = []
while True:
    line = input()
    if not line:
        break
    text.append(line)

end = time()

elapsed_time = (end - start) / 60

chars_count = sum(len(item) for item in text)
words_count = chars_count / 5
wpm = words_count / elapsed_time

print(f"Your average typing speed is {wpm}")

if wpm < 30:
    print("Get better")
elif wpm < 40:
    print("still ahh but keep trying")
elif wpm < 70:
    print("pretty noice")
elif wpm > 80:
    print("Get a job")




