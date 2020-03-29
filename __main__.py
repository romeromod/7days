import xml.etree.ElementTree as ET

CONFIG = {
    "spawning.xml path": "spawning.xml",
    "output_xml_path": "spawning.new.xml",
    "multiplier": 32
}

tree = ET.parse(CONFIG["spawning.xml path"])
root = tree.getroot()

for node in root.findall(".//*[@maxcount]"):
    new_value = int(node.get("maxcount")) * CONFIG["multiplier"]
    node.set("maxcount", str(new_value))

for node in root.findall(".//*[@name='TotalAlive']"):
    values = [
        str(int(value) * CONFIG["multiplier"])
        for value in node.get("value").split(",")
    ]
    new_value = ",".join(values)
    node.set("value", str(new_value))

for node in root.findall(".//*[@name='TotalPerWave']"):
    values = [
        str(int(value) * CONFIG["multiplier"])
        for value in node.get("value").split(",")
    ]
    new_value = ",".join(values)
    node.set("value", str(new_value))

tree.write(CONFIG["output_xml_path"])
