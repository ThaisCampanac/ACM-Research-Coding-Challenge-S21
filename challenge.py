from Bio import SeqIO, GenBank
from Bio.Graphics import GenomeDiagram

content = []
name_to_search = 'ORGANISM'
version_to_search = 'VERSION'
list_of_features = []

def getFile():
    record = SeqIO.read("Genome.gb", "genbank")
    print(record)
    print(record.seq)

    gd_diagram = GenomeDiagram.Diagram(record.id)
    gd_track_for_features = gd_diagram.new_track(2, name="Annotated Features")
    gd_track_for_content = gd_diagram.new_track(1, name ="Annotated Content")
    gd_feature_set = gd_track_for_features.new_set()
    gd_content_set = gd_track_for_content.new_set()
    

    for feature in record.features:
        if feature.type != "gene":
            continue
        if len(gd_feature_set)%2 == 0:
            color = colors.blue
        else:
            color = colors.lightblue
        gd_feature_set.add_feature(feature, color=color, label_size=10, label_angle=0)

    gd_diagram.draw(
        format="circular",
        circular=True,
        pagesize=(20, 20),
        start=10,
        end = len(record),
        circle_core=.7
    )


def main():
    print("Getting contents of the file")
    print()
    getFile()

if __name__ == "__main__":
    main()