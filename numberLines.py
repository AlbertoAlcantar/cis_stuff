def main():
    file_name = name_of_file()

    readFile = open(file_name,'r')

    line = readFile.readline()

    linenumber=1

    while line != '':
        print( str(linenumber) + ':',line.rstrip('\n'))
        line = readFile.readline()
        linenumber = linenumber+1
def name_of_file():
   name=  input('type in the name of the  file:')
   return name
main()