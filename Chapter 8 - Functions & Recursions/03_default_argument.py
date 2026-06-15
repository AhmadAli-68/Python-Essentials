def greet(reply = "Thanks"):
  name = input('What is your name?')
  print(f"Have a nice day, {name}")
  print(f"{name} replies: {reply}")
  return name

greet()