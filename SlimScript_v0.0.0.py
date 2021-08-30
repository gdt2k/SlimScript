global memory1, memory2, memory3
def Do(command,memory1,memory2,memory3):
    memories = ['memory1','memory2','memory3']
    if command == '+':
        if memory1 < 9:
            memory1 += 1
        elif memory1 >= 9:
            memory1 = 0
            if memory2 < 9:
                memory2 += 1
            elif memory2 >= 9:
                memory2 = 0
                if memory3 < 9:
                    memory3 += 1
                else:
                    print('Error: All memory variables are full.')
    elif command == '-':
        if memory1 > 0:
            memory1 -= 1
        elif memory1 == 0:
            if memory2 > 0:
                memory2 -= 1
            elif memory2 == 0:
                if memory3 > 0:
                    memory3 -= 1
                else:
                    print('Error: Memory values cannot be smaller than 0.')
    elif command == 'R':
        memory1 = 0
        memory2 = 0
        memory3 = 0
        print('Memory values have been reset.')
    elif command == 'move':
        a = input('Choose a memory variable to move: ')
        input('Choose a memory variable to move '+ a +' to:')
        if a in memories and input in memories:
            if a == 'memory1':
                if input == 'memory2':
                    memory2 = memory1
                    memory1 = 0
                elif input == 'memory3':
                    memory3 = memory1
                    memory1 = 0
            elif a == 'memory2':
                if input == 'memory1':
                    memory1 = memory2
                    memory2 = 0
                elif input == 'memory3':
                    memory3 = memory2
                    memory2 = 0
            else:
                if input == 'memory1':
                    memory1 = memory3
                    memory3 = 0
                elif input == 'memory2':
                    memory2 = memory3
                    memory3 = 0
            if a == input:
                print('Error: Memory variables cannot be moved to itself.')
                Do('move',memory1,memory2,memory3)
        else:
            print('Error: One or more assigned values isn`t a memory variable. Memory variables are memory1, memory2, and memory3.')
            Do('move',memory1,memory2,memory3)
    elif command == 'del':
        input('Choose a memory variable to delete.')
        if input in memories:
            if input == 'memory1':
                memory1 = 0
            elif input == 'memory2':
                memory2 = 0
            else:
                memory3 = 0
        else:
            print('Error: One or more assigned values isn`t a memory variable. Memory variables are memory1, memory2, and memory3.')
            Do('del',memory1,memory2,memory3)
    elif command == 'copy':
        a = input('Choose a memory variable to copy: ')
        input('Choose a memory variable to copy '+ a +' to:')
        if a in memories and input in memories:
            if a == 'memory1':
                if input == 'memory2':
                    memory2 = memory1
                elif input == 'memory3':
                    memory3 = memory1
            elif a == 'memory2':
                if input == 'memory1':
                    memory1 = memory2
                elif input == 'memory3':
                    memory3 = memory2
            else:
                if input == 'memory1':
                    memory1 = memory3
                elif input == 'memory2':
                    memory2 = memory3
            if a == input:
                print('Error: Memory variables cannot be copied to itself.')
                Do('copy',memory1,memory2,memory3)
        else:
            print('Error: One or more assigned values isn`t a memory variable. Memory variables are memory1, memory2, and memory3.')
            Do('copy',memory1,memory2,memory3)
    elif command == 'slimS.help':
        print('Available commands:\n\n+\n\n-\n\nR\n\nmove\n\ncopy\n\ndel\n\nslimS.help')
def CheckForSyntax():
    availablecommands = ['+','-','R','move','copy','del','slimS.help']
    while True:
        line = input()
        if line in availablecommands: Do(line,memory1,memory2,memory3)
        else: print('Error: Command not supported. Input `slimS.help` for a list of all commands.')
memory1 = 0
memory2 = 0
memory3 = 0
CheckForSyntax()