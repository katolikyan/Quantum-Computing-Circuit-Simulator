little_endian = True

def set_global_endian(setting: str) -> None:
  global little_endian
  if setting != "little-endian" and setting != "big-endian":
    raise ValueError("The argument have to be 'little-endian' or 'big-endian'")
  if setting == "big-endian":
    little_endian = False
  else:
    little_endian = True

# consider to make a class config
