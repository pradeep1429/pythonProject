class MyNumbers:
  def __init__(self):
    self.a = 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.a <=10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()


print(myclass.__next__())
print(myclass.__next__())
print(next(myclass))
print(next(myclass))
print(next(myclass))

for i in myclass:
  print(f"from for {i}")