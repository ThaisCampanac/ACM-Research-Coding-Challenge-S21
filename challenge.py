content = []
name_to_search = 'ORGANISM'
version_to_search = 'VERSION'
list_of_features = []

def getFile():
    f = open("Genome.gb", "r")

    f1 = f.readlines()

    for x in f1:
        content.append(x.strip())
        if name_to_search in x:
            list_of_features.append(x.strip())
        if version_to_search in x:
            list_of_features.append(x.strip())
    print(list_of_features)


def main():
    print("Getting contents of the file")
    print()
    getFile()

if __name__ == "__main__":
    main()