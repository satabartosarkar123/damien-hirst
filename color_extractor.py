import colorgram # type: ignore
def extract_colors(img:__file__,n:int)->list:
    """Either use the colorgram library to extract colors from an image or use a predefined palette.
    you can choose to use any image , please change the file name from "img.jpg" to anything you like.(in which you image is saved). Pass in m as the number of colours to be extracted """
    color=colorgram.extract(img, n)
    palette= [c.rgb for c in color]
    return palette

