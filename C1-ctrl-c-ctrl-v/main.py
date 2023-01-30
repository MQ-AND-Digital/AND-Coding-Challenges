from strings import *

def findNextCommand(str):
  lowestIndex = len(str)
  nextCommand = ""

  for command in ["[CTRL+C]", "[CTRL+X]"]:
    if (0 <= str.find(command) < lowestIndex):
      lowestIndex = str.find(command)
      nextCommand = command
  
  return nextCommand

def modifyString(original):
  s = original
  next = findNextCommand(s)

  while (next != ""):
    copyEnd = s.index(next)
    copied = s[0:copyEnd]

    if next == "[CTRL+C]":
      s = s.replace(next, "", 1)
    elif next == "[CTRL+X]":
      s = s[copyEnd: ].replace(next, "", 1)

    pasteStart = s.index("[CTRL+V]")
    s = (s[ :pasteStart] + copied + s[pasteStart: ]).replace("[CTRL+V]", "", 1)

    next = findNextCommand(s)

  cleanedString = s.replace("[CTRL+C]", "").replace("[CTRL+V]", "").replace("[CTRL+X]", "").replace("  ", " ").strip()
  return cleanedString

print(modifyString(stringsList[0]))