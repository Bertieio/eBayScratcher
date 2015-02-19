import urllib2
import elementtree
import glob
from time import gmtime, strftime


def Pos(PageData):
	Pos1 = 0
	PosS = Pos1
	while PageData[PosS:PosS+1] == ' ' or PageData[PosS:PosS+1] == '-':
		PosS = PosS + 1
	PosE = 0
	while PageData[PosE:PosE+1] != '<':
		PosE = PosE + 1
	print PageData[PosS:PosE]
	
log = open('log.txt','w')	
	
wURL = 'http://www.ebay.co.uk/itm/161333231002'

print wURL 

itemURL = urllib2.urlopen(wURL)

itemDetails = itemURL.read()

toFind = 'Our Number'

ourPos = itemDetails.find(toFind)
if ourPos == -1:
	print 'Not found'
	log.write('no number '+ wURL +' time: ' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '\n')
else:	
	ourPos = ourPos + 10
	itemData = itemDetails[ourPos:ourPos+15]
	Pos(itemData)
	
print 'Done'

log.close()
