import xml.etree.cElementTree as ET
import xml.dom.minidom as minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


def createXML(folderName, fileName, width, height, depth, name, x1, y1, x2, y2, dir):

    annotation = ET.Element('annotation')

    ET.SubElement(annotation, 'folder').text = folderName
    ET.SubElement(annotation, 'filename').text = fileName

    size = ET.SubElement(annotation, 'size')

    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)

    object = ET.SubElement(annotation, 'object')
    ET.SubElement(object, 'chair')
    bndbox = ET.SubElement(object, 'bndbox')
    ET.SubElement(bndbox, 'xmin').text = str(x1)
    ET.SubElement(bndbox, 'ymin').text = str(y2)
    ET.SubElement(bndbox, 'xmax').text = str(x2)
    ET.SubElement(bndbox, 'ymax').text = str(y2)

    tree = ET.ElementTree(annotation)
    treeString = prettify(annotation)

    treeString = treeString[treeString.find('\n') + 1: treeString.rfind('\n')]
    with open(dir + fileName.split('.')[0] + '.xml', 'w') as xml_file:
        xml_file.write(treeString)

    # tree.write(fileName + '.xml')
if __name__ == '__main__':
    pass