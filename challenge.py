from Bio import SeqIO, GenBank
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Graphics import GenomeDiagram
from reportlab.lib import colors
from reportlab.lib.units import cm

def getFile():
    #reading the file
    record = SeqIO.read("Genome.gb", "genbank")
    print(record)

    #making the gd_diagram for the genome
    gd_diagram = GenomeDiagram.Diagram(record.id)
    gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
    gd_feature_set = gd_track_for_features.new_set()
    gd_track_for_content = gd_diagram.new_track(4, name= "Annotated Content")
    gd_content_set = gd_track_for_content.new_set()

    #adding the features to the gd_diagram
    for feature in record.features:
        if feature.type != "gene":
            continue
        if len(gd_feature_set)%2 == 0:
            color = colors.blue
        else:
            color = colors.lightblue
        gd_feature_set.add_feature(feature, color=color, label=True, label_size=15, label_angle=0)

    #adding the DNA sequence to the diagram
    list_of_dna = []
    index = 1
    dna = ""
    for seq in record.seq:
        dna = dna + seq
        if (index)%10 == 0:
            list_of_dna.append(dna)
            dna = ""
        index = index + 1

    for x in list_of_dna:
        index = 0
        while True:
            index = record.seq.find(x, start=index)
            if index == -1:
                break
            feature = SeqFeature(FeatureLocation(index, index + len(x)))
            gd_content_set.add_feature(
                feature,
                color=colors.green,
                name = x,
                label=True,
                label_size=5,
            )
            index += len(x)
        

    #making the circular diagram
    gd_diagram.draw(
        format="circular",
        circular=True,
        pagesize=(60 * cm, 60 * cm),
        start=0,
        end = len(record),
        circle_core=.5
    )

    #writing the diagram to all formats asked by the client
    gd_diagram.write("genome_circular_diagram.png", "PNG")


def main():
    print("Getting contents of the file")
    print()
    getFile()

if __name__ == "__main__":
    main()