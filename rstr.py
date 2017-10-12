def thtm(f,s):
	f = open(f,"+a") #opens file with name of "test.txt"
	f.write(s)
	f.close()

i = 0;
for l in open('Ayat-Koleksi.htm'):
	i +=1
	dn = 'b'+str(i)
	px = "'px'"
	ll = l.replace('target="mframe"',r'onclick="myFunction(\''+dn+'\')" target="'+dn+'"')
	ll = ll.replace('\\','')
	thtm('index.html',ll)
	if 'a href=' in ll:
		thtm('index.html','<div id="'+dn+'" style="display:none;"><iframe name="'+dn+'" src="" style="border: none; " width="100%" onload="this.style.height=this.contentDocument.body.scrollHeight +'+px+';"></iframe></div>\n')
