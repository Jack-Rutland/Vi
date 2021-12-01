import commands
from dispatch_table import dispatch_table

def main() :
    command = input('Please provide a command!\n')
    command_split = command.split(' ')
    print(f'Executing "{command}"...')
    dispatch_table[command_split[0]](*command_split[1:])

if __name__ == '__main__' :
    main()