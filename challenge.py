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
    

    #adding the features to the gd_diagram
    for feature in record.features:
        if feature.type != "gene":
            continue
        if len(gd_feature_set)%2 == 0:
            color = colors.blue
        else:
            color = colors.lightblue
        gd_feature_set.add_feature(feature, color=color, label_size=10, label_angle=0)


    #making the circular diagram
    gd_diagram.draw(
        format="circular",
        circular=True,
        pagesize=(20 * cm, 20 * cm),
        start=10,
        end = len(record),
        circle_core=.7
    )

    #writing the diagram to all formats asked by the client
    gd_diagram.write("genome_circular_diagram.png", "PNG")
    gd_diagram.write("genome_circular_diagram.jpeg", "JPEG")
    gd_diagram.write("genome_circular_diagram.jpg", "JPG")


def main():
    print("Getting contents of the file")
    print()
    getFile()

if __name__ == "__main__":
    main()