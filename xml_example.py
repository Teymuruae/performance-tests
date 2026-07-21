import xml.etree.ElementTree as ET

xml_str = """
<user>
    <name>Иван</name>
    <age>33</age>
    <address>
        <country>Russia</country>
        <city>Moscow</city>
    </address>
</user>
"""

root = ET.fromstring(xml_str)

country = root.find('address').find('country').text

with open('user.xml', encoding='utf-8') as file:
    parsed_xml = ET.parse(file)
    parsed_root = parsed_xml.getroot()

print(parsed_root.find('address').find('city').text)
