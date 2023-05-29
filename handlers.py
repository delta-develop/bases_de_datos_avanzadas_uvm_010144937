import os
import xml.etree.ElementTree as ET
import xmltodict
import json

OUTPUT_FILE = "output.xml"
HTML_OUTPUT_FILE = "static/output.html"

def save_to_xml(data):

    if not os.path.exists("output.xml"):
        root, tree = create_xml()
    else:
        root, tree = use_existing_xml()
    
    add_to_xml(data, root, tree)

def use_existing_xml():
    tree = ET.parse(OUTPUT_FILE)
    root = tree.getroot()

    return root, tree

def create_xml():
    root = ET.Element("root")
    tree = ET.ElementTree(root)
    return root,tree

def add_to_xml(data, root, tree):
    json_to_xml(data,root)
    tree.write("output.xml", encoding="utf-8", xml_declaration=True)


def json_to_xml(json_data, parent):
    for key, value in json_data.items():
        if isinstance(value,dict):
            child = ET.Element(key)
            parent.append(child)
            json_to_xml(value, child)
        else:   
            child = ET.Element(key)
            child.text = str(value)
            parent.append(child)


def xml_registers_to_json():
    with open(OUTPUT_FILE) as xml_file:
        json_data = xmltodict.parse(xml_file.read())
        root = json_data["root"]
        empleoyees = root["empleoyee"]

        for empleoyee in empleoyees:
            yield empleoyee
       

def write_to_html():
    with open(HTML_OUTPUT_FILE,"w") as html_file:
        html_file.write("""
        <html>
            <head>Registros guardados</head>
            <body>
                <table>
                    <tr>
                        <th>Nombre</th>
                        <th>Apellidos</th>
                        <th>Edad</th>
                        <th>Sexo</th>
                        <th>Puesto</th>
                    </tr>
        """)

        for empleoyee in xml_registers_to_json():
            html_file.write(
                f"""
                <tr>
                    <td>{empleoyee["name"]}</td>
                    <td>{empleoyee["lastname"]}</td>
                    <td>{empleoyee["age"]}</td>
                    <td>{empleoyee["sex"]}</td>
                    <td>{empleoyee["position"]}</td>
                </tr>
                """
            )
        
        html_file.write("""
                </table>
            </body>
        </html>
        """)
    
    return

