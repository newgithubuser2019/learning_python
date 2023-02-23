try:
  with open("fn.txt", "r") as fh:
    var = fh.read()
except FileNotFoundError:
  print("not found")