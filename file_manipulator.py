import sys

def reverse(inputpath,outputpath):
    with open(inputpath) as f:
        contents = f.read()
    
    with open(outputpath, 'w') as f:
        revContents = contents[::-1]
        f.write(revContents)

def copy(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()
    
    with open(outputpath, 'w') as f:
        f.write(contents)

def duplicate(inputpath,n):
    with open(inputpath) as f:
        contents = f.read()
    
    dupContents = ''
    for i in range(int(n)):
        dupContents = dupContents + contents
    
    with open(inputpath,'w') as f:
        f.write(dupContents)

def replace(inputpath,org,sub):
    with open(inputpath) as f:
        contents = f.read()

    repContents = contents.replace(org,sub)
    
    with open(inputpath,'w') as f:
        f.write(repContents)

def validate_argv(expLen):
    if len(sys.argv) != expLen:
        print(f"Error: Expected {expLen -1} arguments, but got {len(sys.argv) -1}.")
        sys.exit(1)

match sys.argv[1]:
    case 'reverse':
        validate_argv(4)
        reverse(sys.argv[2], sys.argv[3])
    case 'copy':
        validate_argv(4)
        copy(sys.argv[2], sys.argv[3])
    case 'duplicate-contents':
        validate_argv(4)
        duplicate(sys.argv[2], sys.argv[3])
    case 'replace-string':
        validate_argv(5)
        replace(sys.argv[2], sys.argv[3], sys.argv[4])
    case _:
        print("Error: Unknown command.")
        sys.exit(1)