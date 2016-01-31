from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import re
from urllib import urlopen
import nltk
def clean_html(html):
	"""
 Remove HTML markup from the given string.

    :param html: the HTML string to be cleaned
    :type html: str
    :rtype: str
    """

	# First we remove inline JavaScript/CSS:
	cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
	# Then we remove html comments. This has to be done before removing regular
	# tags since comments can contain '>' characters.
	cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
	# Next we can remove the remaining tags:
	cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
	# Finally, we deal with whitespace
	cleaned = re.sub(r"&nbsp;", " ", cleaned)
	cleaned = re.sub(r"  ", " ", cleaned)
	cleaned = re.sub(r"  ", " ", cleaned)
	return cleaned.strip()

url="http://www.behindthename.com/"
html=urlopen(url).read()
raw=clean_html(html)
print(raw)
html_page = urllib2.urlopen("http://www.behindthename.com/")
soup = BeautifulSoup(html_page)
final_dic={}
f=open('A_names1.html','w')
for link in soup.findAll('a'):
               #link= soup.findAll('a', attrs={'href': re.)})
               test= link.get('href')
               #####open html file
               if re.match(r'(.*)letter/a',test):
                       land="".join(["http://www.behindthename.com",test])
                       print land
                       for link in land[:1]:
                               url1=land
                               #page1=urllib.urlopen(url1)
                               #soup=BeautifulSoup(page1)
                               html1=urlopen(url1).read()
                               new_str=''
                               for each in html1:
                                       new_str+=each.strip()
                               print ("new_str", new_str)
                               result=re.findall('<b><(ahref="/name/.*?)">(.*?)</a></b>',new_str)
                               #new_strr=''
                               #declare dict

                               result_dic={}
                               for res in result:
                                       link=res[0]
                                       name=res[1]
                                       result_dic[name]=link
                               #print result_dic
                               #sys.exit()
                               for name in result_dic:
                                       #if name !='AABRAHAM':
                                               #continue
                                       result=result_dic[name]
                                       result_list=result.split('"')
                                       parurl=result_list[1]
                                       urln="".join(["http://www.behindthename.com",parurl])
                                       url2=urln
                                       #page2=urllib.urlopen(url2)
                                       #soup=BeautifulSoup(page2)
                                       html2=urlopen(url2).read()
                                       new_str1=''
                                       for each in html2:
                                               new_str1+=each.strip('\n')
                                       #result1=re.findall('<span class="namesub">(GENDER:)</span> <span class="info"><span class="(.*?)>(.*?)</span></span></div>',new_str1)
                                       print name       #print new_str1
                                       result1=re.findall('<span class="namesub">(GENDER:)</span> <span class="info"><span class=".*?">(.*?)</span>',new_str1)
                                       #res1=str(result1)
                                       result2=re.findall('<span class="namesub">(USAGE:)</span> <span class="info"><a href="/names/usage/.*" class="usg">(.*?)</a></span></div>',new_str1)
                                       #print result2
                                       #sys.exit()
                                       #res2=str(result2)
                                       result3=re.findall('<span class="namesub">(PRONOUNCED:)</span> <span class="info">(.*?)</span>',new_str1)
                                       #print result3
                                       #sys.exit()
                                       #res3=str(result3)
                                       new_result1=[]
                                       new_result2=[]
                                       new_result3=[]
                                       #if re.match(r'(.*?)<(.*?)>(.*)',res1):
                                                #result1=re.sub('<(.*?)>','',res1)
                                        #if re.match(r'(.*?)<(.*?)>(.*?)',res2):
                                                #result2=re.sub('<(.*?)>','',res2)
                                                #if re.match('(.*?)class="usg>(.*?)',result2):
                                                       #resn=result2
                                                       #result2=re.sub('class="usg">','',resn)
                                       #if re.match(r'(.*?)<(.*?)>(.*?)',res3):
                                                #result3=re.sub('<(.*?)>','',res3)
                                       for elm in result1:
                                                new_result1.append(elm[0]+''+elm[1])
                                       for elm1 in result2:
                                                new_result2.append(elm1[0]+''+elm1[1])
                                       for elm2 in result3:
                                           if elm2:
                                                #print elm2[0]
                                                #print elm2[1] 
                                                new_result3.append(elm2[0]+''+elm2[1])
                                       #print new_result3
                                       #sys.exit()
                                       res1=str(new_result1)
                                       res2=str(new_result2)
                                       res3=str(new_result3)
                                       nnew_result1=[]
                                       nnew_result2=[]
                                       nnew_result3=[]
                                       if re.match(r'(.*?)<(.*?)>(.*?)',res1):
                                               nnew_result1=re.sub('<(.*?)>','',res1)
                                       else:
                                               nnew_result1=new_result1
                                       if re.match(r'(.*?)<(.*?)>(.*?)',res2):
                                               nnew_result2=re.sub('<(.*?)>','',res2)
                                               if re.match(r'(.*?)class="usg">(>*?)',new_result2):
                                                       resn=new_result2
                                                       nnew_result2=re.sub('class="usg">','',new_result2)
                                       else:
                                               nnew_result2=new_result2
                                       if re.match(r'(.*?)<(.*?)>(.*?)',res3):
                                               nnew_result3=re.sub('<(.*?)>','',res3)
                                       else:
                                               nnew_result3=new_result3
                                       list1=[''.join(nnew_result1),''.join(nnew_result2),''.join(nnew_result3)]
                                       final_dic[name]=list1

print("RESULT:", final_dic)
f.write('<html>')
f.write('<table border="1">')
f.write('<tr>')
f.write('<td>')
f.write('<th>Names and Details</th>')
f.write('</td>')
f.write('</tr>')
for k in final_dic.keys():
       v = final_dic[k]
       f.write('<tr>')
       f.write('<td>'+k+'</td>')
       f.write('<td> '+'<br>'.join(v)+'</td>')
       f.write('</tr>')
f.write('</table>')
f.write('</html>')
