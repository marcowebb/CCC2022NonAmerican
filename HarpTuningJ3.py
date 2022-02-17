instructions = input()
instructions = [i for i in instructions]
turnsNum = 0
throwaway = 0
noteLetters = ""

for i in range(0, len(instructions)):
    if instructions[i] == "+":
        turnsNum = instructions[i + 1]
        print(noteLetters, "tighten", turnsNum)
        noteLetters = ""

    elif instructions[i] == "-":
        turnsNum = instructions[i + 1]
        print(noteLetters, "loosen", turnsNum)
        noteLetters = ""

    elif instructions[i - 1] == "+" or instructions[i - 1] == "-":
        throwaway += 1

    else:
        noteLetters = noteLetters + instructions[i]
