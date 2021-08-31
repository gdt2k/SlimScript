global availablecommands, memory
availablecommands = ['+','-','R','move','copy','del','rpt','rng','memory','memories','slimS.help','slimS.guide','M1','M2','M3','S1','S2','S3','Sp1']
import time, random
def Guide(command):
    if command == '+': print('\nAdds 1 to one of the memory values.')
    elif command == '-': print('\nRemoves 1 from one of the memory values.')
    elif command == 'R': print('\nResets all memory values` contents.')
    elif command == 'move': print('\nMoves a memory value`s contents to another one.')
    elif command == 'copy': print('\nCopies a memory value`s contents to another one. ')
    elif command == 'del': print('\nResets a memory value`s contents.')
    elif command == 'rpt': print('\nRepeats the specified command X times.')
    elif command == 'rng': print('\nSets all memory values to a random number.')
    elif command == 'memory': print('\nDisplays the memory values.')
    elif command == 'memories': print('\nDisplays the names of the memory values.')
    elif command == 'slimS.help': print('\nDisplays the available commands.')
    elif command == 'slimS.guide': print('\nDisplays the guide for a command.')
    elif command == 'slimS.variableGuide': print('\nDisplays the guide for variables.')
    elif command == 'slimS.guide': print('\nDisplays the guide for a command.')
    elif 'M' in command or 'S' in command: print('\nDisplays an error and the cause.')
def Do(command):
    global memories1,memories2,memories3
    memory = [memories1,memories2,memories3]
    memories = ['memories1','memories2','memories3']
    if command == '+':
        if memories1 < 9: memories1 = memories1 + 1
        elif memories1 >= 9:
            memories1 = 0
            if memories2 < 9: memories2 = memories2 + 1
            elif memories2 >= 9:
                memories2 = 0
                if memories3 < 9: memories3 = memories3 + 1
                else: print('MemoryError: memory is full. (Error: M1)')
    elif command == '-':
        if memories1 > 0: memories1 -= 1
        elif memories1 == 0:
            if memories2 > 0: memories2 -= 1
            elif memories2 == 0:
                if memories3 > 0: memories3 -= 1
                else: print('MemoryError: memory values are empty. (Error: M2)')
    elif command == 'R':
        memories1 = memories2 = memories3 = 0
        print('Memory values have been reset.')
    elif command == 'move':
        a = input('Choose a memory value to move: ')
        input('Choose a memory value to move '+ a +' to: ')
        if a in memories and input in memories:
            if a == 'memories1':
                if input == 'memories2':
                    memories2 = memories1
                    memories1 = 0
                elif input == 'memories3':
                    memories3 = memories1
                    memories1 = 0
            elif a == 'memories2':
                if input == 'memories1':
                    memories1 = memories2
                    memories2 = 0
                elif input == 'memories3':
                    memories3 = memories2
                    memories2 = 0
            else:
                if input == 'memories1':
                    memories1 = memories3
                    memories3 = 0
                elif input == 'memories2':
                    memories2 = memories3
                    memories3 = 0
            if a == input:
                print('SyntaxError: unexpected match between value 1 and value 2. (Error: S2)')
                Do('move',memories1,memories2,memories3)
        else:
            print('SyntaxError: assigned values not found in memories. (Error: S1)')
            Do('memories',memories1,memories2,memories3)
            Do('move',memories1,memories2,memories3)
    elif command == 'copy':
        a = input('Choose a memory variable to copy: ')
        input('Choose a memory variable to copy '+ a +' to: ')
        if a in memories and input in memories:
            if a == 'memories1':
                if input == 'memories2': memories2 = memories1
                elif input == 'memories3': memories3 = memories1
            elif a == 'memories2':
                if input == 'memories1': memories1 = memories2
                elif input == 'memories3': memories3 = memories2
            else:
                if input == 'memories1': memories1 = memories3
                elif input == 'memories2': memories2 = memories3
            if a == input:
                print('SyntaxError: unexpected match between value 1 and value 2. (Error: S2)')
                Do('copy',memories1,memories2,memories3)
        else:
            print('SyntaxError: assigned values not found in memories. (Error: S1)')
            Do('memories',memories1,memories2,memories3)
            Do('copy',memories1,memories2,memories3)
    elif command == 'del':
        input('Choose a memory variable to delete. ')
        if input in memories:
            if input == 'memories1':
                if memories1 < 0: print()
            if input == 'memories1':
                memories1 = 0
            elif input == 'memories2': memories2 = 0
            else: memories3 = 0
        else:
            print('SyntaxError: assigned values not found in memories. (Error: S1) ')
            Do('del')
    elif command == 'rpt':
        a = input('Choose a command to repeat: ')
        b = int(input('Repeat '+ a +' how many times? '))
        if b < 101:
            for i in range(b):
                Do(a)
                time.sleep(0.05)
        else: print('SpecialError: value too great for command. (Error: Sp1)')
    elif command == 'rng':
        input('Choose a memory value to affect. (Type `all` to affect all values) ')
        if input in memories:
            if input == 'memories1':
                memories1 = random.randint(0,9)
            elif input == 'memories2':
                memories2 = random.randint(0,9)
            elif input == 'memories3':
                memories3 = random.randint(0,9)
        elif input == 'all':
            memories1 = random.randint(0,9)
            memories2 = random.randint(0,9)
            memories3 = random.randint(0,9)
        else:
            print('SyntaxError: input not found in availablecommands. (Error: S3)')
            Do('rng')
    elif command == 'memory': print(memory)
    elif command == 'memories': print('Memory value names:\nmemories1\nmemories2\nmemories3')
    elif command == 'slimS.help': print('Available commands:',availablecommands)
    elif command == 'slimS.guide':
        c = input('Choose a command to get info on. ')
        if c in availablecommands: Guide(c)
        else: print('SyntaxError: input not found in availablecommands. (Error: S3)')
    elif command == 'M1': print('MemoryError: memory is full. (Value >= 1110)')
    elif command == 'M2': print('MemoryError: memory values are empty. (Value <= 0)')
    elif command == 'M3': print('MemoryError: memory values are not in range or not of class int. (Values are corrupted)')
    elif command == 'S1': print('SyntaxError: assigned values not found in availablecommands. (Input isn`t a command)')
    elif command == 'S2': print('SyntaxError: unexpected match between value 1 and value 2. (A memory value can`t affect itself.)')
    elif command == 'S3': print('SyntaxError: input not found in availablecommands. (Not a command)')
    elif command == 'Sp1': print('SpecialError: value too great for command. (Cap reached)')
def CheckForSyntax():
    line = input(' ')
    if line in availablecommands: Do(line)
    else: print('SyntaxError: input not found in availablecommands. (Error: S3)')
memories1 = memories2 = memories3 = 0
totalmemory = int(str(memories3 + memories2 + memories1))
while True: CheckForSyntax()