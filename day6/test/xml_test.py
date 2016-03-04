#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
print(root)
#遍历xml文档
for child in root:
    print(child.tag,"-->名称",child.attrib,"-->属性")
    for i in child:
        print(i.tag, i.text)



#只遍历year 节点
for node in root.iter("year"):
    print(node.tag,node.text)

#修改和删除xml文档内容
import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()

for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated","yes")

tree.write("test1.xml")

#删除node
for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
     root.remove(country)

tree.write('output.xml')
