def main():
    fo = open("./test.txt")
    line = fo.read()
    print(line)
    fo.close()

if __name__== "__main__":
    main()