# This script coverts Words to {Words} in lines starting with the word Title
# Useful for bib files used with the longbibliography option

# input file
f = open("main2.bib", "r")

# output file
copy = open("main.bib", "w")


for line in f:
    if (line.find('Article', 0, 20) > 0):
        matchStart = line.find('{')
        matchEnd = line.find(',')
        print("Looking at " + line[ matchStart+1 : matchEnd ])
    if (line.find('Title', 0, 20) > 0):
	splitline = line.split(" ")
	matchStart = [x for x in splitline if x.find('{')>=0]
	matchEnd = [x for x in splitline if x.find('}')>=0]
	nstart = splitline.index(matchStart[0])
	nend = splitline.index(matchEnd[0])
	for i in range(nstart,nend+1):
	  if len(splitline[i])>1:
	    # if starts with {
	    if ((splitline[i][0]=='{' and splitline[i][1].isupper()) and splitline[i].find('}')<0):
	      splitline[i] = '{' + splitline[i] + '}'
            # if ends with }
	    if ((splitline[i].find('}')>=0 and splitline[i][0].isupper()) and splitline[i].find('{')<0):
	      temp = splitline[i].find('}')
	      splitline[i] = '{' + splitline[i][:temp] + '}' + splitline[i][temp:]
            # if does not have {} - avoid doubling the work
            if (splitline[i].find('{')<0 and splitline[i].find('}')<0):
	      if splitline[i][0].isupper():
                splitline[i] = '{' + splitline[i] + '}'
	    line = " ".join(splitline)
        print("Done.")
    copy.write(line)
f.close()
copy.close()
