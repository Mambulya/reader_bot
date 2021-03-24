"""
There is the whole project data: fonts, colors, backs
"""

fonts = ["Abram", "Capuletty", "Djiovanni", "Merkucio"]
colors_hex = {
              "purple-blue": '#2e2b6e',
              "black" : "#010101",
              "blue": "#132C7D",
              "blueM" : "#1C2865",
              }

# NOTE: (blue, green, red)
colors_rgb = {
              'purple-blue' : (46, 43, 110, 240),
              'black': (61, 61, 61, 256),
              'blue': (19, 44, 125, 256),
              "blueM" : (28, 40, 100)
            }


class IntPaper:
    """
    Key word for this type paper - k
    given a matrix DIMENSIONS. Every paper class has its own one respectively.
    For example, if a user has chosen font 1 on a checkered paper, then
        line = IntPaper.DIMENSIONS[0][1]
        size = IntPaper.DIMENSIONS[1][1]
        start_x = IntPaper.DIMENSIONS[2]
    """
    PATH = r'BACKs/good/graph.png'
    DIMENSIONS = [
                [50, 38, 48, 46],  # line for font: 0, 1, 2, 3
                [50, 42, 43, 43],   # size for font: 0, 1, 2, 3
                192]                # start_x

    Y_POS = (34, 68, 102, 138, 172, 206, 241, 275, 310, 345, 379, 413, 448, 483,
         517, 552,587, 620, 656, 691, 725, 759, 794, 828, 864, 899, 933, 968,
         1003, 1037, 1071,1107, 1142, 1175, 1210, 1245, 1280, 1314, 1349)


class LinePaper:
    """
    Key word for this type paper - l
    Check the IntPaper class documentation
    """
    PATH = r'BACKs/good/lined.png'
    DIMENSIONS = [
        [48, 45, 51, 51],
        [51, 35, 35, 34],
        45]
    Y_POS = (82, 134, 190, 242, 294, 348, 400, 454, 506, 562, 614, 668, 722, 776, 830, 880, 936, 990, 1042, 1096, 1148, 1202, 1254)


class A4:
    """
    Key word for this type paper - b
    Check the IntPaper class documentation if questions appear
    """
    PATH = r'BACKs/good/A4.png'
    DIMENSIONS = [
        [67, 55, 65, 65],
        [50, 42, 42, 41],
        63]
    Y_POS = IntPaper.Y_POS