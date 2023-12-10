import json
import html

def readJsonFile(filename):
    with open(filename, 'r') as target_file:
        target_data = json.load(target_file)
        return target_data
    
def htmlStrComposer(jsonObject):
    subDomExisted = 'children' in jsonObject[0].keys()
    generatedHtml = ''
    generatedStyle = ''
    
    if (subDomExisted == False):
        attrObject = jsonObject[0]['attributes']
        tagName = attrObject['tagName']
        generatedHtml += '<' + tagName
        for key, value in attrObject.items():
            if(key == 'className'):
                generatedHtml += ' class="' + value + '"'
        if 'style' in attrObject.keys():
            generatedStyle += ' style="'
            for styleKey, styleValue in jsonObject[0]['attributes']['style'].items():
                generatedStyle += styleKey + ': ' + styleValue + '; '
            
            generatedStyle = generatedStyle[:-1] + '"'
        generatedHtml += generatedStyle + '></' + tagName + '>'
        
    else:
        attrObject = jsonObject[0]['attributes']
        tagName = attrObject['tagName']
        generatedHtml += '<' + tagName
        for key, value in attrObject.items():
            if(key == 'className'):
                generatedHtml += ' class="' + value + '"'
        if 'style' in attrObject.keys():
            generatedStyle += ' style="'
            for styleKey, styleValue in jsonObject[0]['attributes']['style'].items():
                generatedStyle += styleKey + ': ' + styleValue + '; '
            generatedStyle = generatedStyle[:-1] + '"'
        generatedHtml += generatedStyle + '>'
        
        childDomContainer = ''
        for subDom in jsonObject[0]['children']:
            childDomContainer += htmlStrComposer(subDom)
        generatedHtml += childDomContainer + '</' + tagName + '>'
    
    return generatedHtml

def json2html(filename):
    return htmlStrComposer(readJsonFile(filename))
