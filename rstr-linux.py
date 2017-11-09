'''
Script ini untuk mengubah halaman --Ayat-Koleksi.htm-- menjadi --index.html--
digunakan di windows CMD, 
How to : 
	1. buka CMD, 
	2. Masuk ke Direktori script ini berada dengan perintah : --CD X:\Contoh\Folder\qweb--
	3. ketik perintah : --python rstr.py-- lalu ENTER 
	4. Selesai,
-----------------------
NB : 	Jika mau Update Ayat Koleksi, Lakukan Update pada file --Ayat-Koleksi.htm-- 
		Setelah update selesai, lakukan instruksi sebagaimana di --How to--
'''
def deleteContent(fName):
    with open(fName, "w"):
        pass
	
def thtm(f,s):
	f = open(f,"a") #opens file with name of "test.txt"
	f.write(s)
	f.close()
	
deleteContent('index.html')
i = 0;
for l in open('Ayat-Koleksi.htm'):
	
	i +=1
	dn = 'b'+str(i)
	px = "'px'"
	ll = l.replace('target="mframe"',r'onclick="myFunction(\''+dn+'\')" target="'+dn+'"')
	ll = ll.replace('\\','')
	ll = ll.replace('index.html','old-index.htm')
	ll = ll.replace('New Page','Old Page')
	thtm('index.html',ll)
	if 'a href=' in ll and 'Al-Quran' in ll:
		thtm('index.html','<div id="'+dn+'" style="display:none;"><iframe name="'+dn+'" src="" style="border: none; " width="100%" onload="this.style.height=this.contentDocument.body.scrollHeight +'+px+';"></iframe></div>\n')
