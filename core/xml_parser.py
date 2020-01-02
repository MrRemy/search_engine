import os
import xml.etree.ElementTree as et


class Article:
    def __init__(self, title, description, link):
        self.title = title
        self.description = description
        self.link = link


def init_data():
    files = []
    for file in os.listdir("../articles"):
        if file.endswith(".xml"):
            files.append(open(os.path.join("../articles", file), encoding='utf8'))
            # print(os.path.join("/mydir", file))

    return files


def parser(files):
    parsed_list = []
    for file in files:
        tree = et.parse(file)
        doc = tree.getroot()
        doc = doc.find('channel')
        for e in doc.iter('item'):
            # article = et.tostring(e, encoding='unicode', method='text').strip()
            parsed_list.append(Article(e.findtext('title'), e.findtext('description'), e.findtext('link')))

    return parsed_list
