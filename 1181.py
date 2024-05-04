#1181
n = int(input())
words = []
for _ in range(n):
  words.append(input())
words = set(words)
words = list(words)
words.sort()
words = sorted(words, key = lambda x: len(x))
for word in words:
  print(word)
