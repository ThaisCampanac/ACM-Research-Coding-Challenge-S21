def getFile():
    f = open("Genome.gb")
    for line in f:
        line = line.strip()
        for word in line.split():
            if word == "Source":
            #take line after that

def main():
    print("Getting contents of the file")
    getFile()

if __name__ == "__main__":
    main()