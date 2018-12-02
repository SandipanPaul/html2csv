import urllib
import csv


def cleanUrl(page):
    npage = ''
    occur = 1
    stat = True
    while occur > 0:
        occur = page.find(',,')
        if occur > 0:
            npage += page[0:occur + 1]
            npage += 'NULL,'
            page = page[occur + 2:len(page)]
        stat = False
    if not stat:
        npage += page[0:len(page)]
        page = npage
    return page

def businessLogic(n):
    i=int(n)


# can be done in one liner but this is more efficient in terms on space and time complexity
def createList(page):
    npage = []
    occur = 1
    while occur > 0:
        occur = page.find('\n')
        if occur > 0:
            txt = list(page[0:occur - 1].split(','))
            # for i in range(0,len(txt)):
            #     txt[i]=businessLogic(txt[i]) #Apply business logic here
            npage.append(txt)
            page = page[occur + 1:len(page)]
    txt = list(page[0:len(page)].split(','))
    npage.append(txt)
    return npage


def checkHeader(page):
    occur = page.find('\r')
    txt = page[0:occur].split(',')
    for i in txt:
        try:
            int(i)
            return False
        except ValueError:
            continue
    return True


url = 'new1.html'  # replace with the html returned from the web api
page = urllib.urlopen(url).read().replace('|', ',').replace(';', ',').replace('\t', ',').replace(',', ',')
if checkHeader(page):
    page = cleanUrl(page)
    page = createList(page)
else:
    raise Exception('Invalid header format')
with open('out.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(page)

writeFile.close()
