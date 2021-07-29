import xml.etree.ElementTree as ET
with open('xml_example.xml', 'r') as file:
    mytree = ET.parse(file)
    myroot = mytree.getroot()
user = myroot.find('user')
print(user.find('name').text)
for role in user.findall('roles'):
    print(role.text)

user.find('location').find('city').text = "Dallas"
with open('xml-edited.xml', 'w') as file2:
   mytree.write(file2, encoding='unicode')
