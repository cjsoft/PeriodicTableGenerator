#coding=utf-8

comm = """<?xml version="1.0" encoding="utf-8"?>
<!-- 班服自动化  -->
<svg version="1.1" id="MainLayer" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 510 637.1" style="enable-background:new 0 0 510 637.1;" xml:space="preserve">
<style type="text/css">
	.st0{fill:none;stroke:#C9CACA;stroke-width:10;stroke-miterlimit:10;}
	.st1{font-family:'Chantilly-Serial-Regular';}
	.st2{font-size:90.9864px;}
	.st3{font-size:307.3865px;}
	.st4{font-size:98.3637px;}
   	.st5{letter-spacing:-3.3;}
   	.st6{letter-spacing:-6.3;}
   	.st7{letter-spacing:-9.3;}
    .end{text-anchor:end;}
    .start{text-anchor:start;}
    .middle{text-anchor:middle;}
</style>
"""
rstr1="""
{0}
<rect id="XMLID_3_" x="5" y="5" class="st0" width="500" height="627.1"/>
<text id="XMLID_4_" x="30" y="100" class="st1 st2">{1}</text>
<text id="XMLID_5_" x="255" y="370" class="st1 st3 middle">{2}</text>
<text id="XMLID_6_" x="255" y="500" class="st1 st4 middle">{3}</text>
<text id="XMLID_7_" x="480" y="595" class="st1 st2 end">{4}</text>
</svg>
"""
rstr2="""
{0}
<rect id="XMLID_3_" x="5" y="5" class="st0" width="500" height="627.1"/>
<text id="XMLID_4_" x="30" y="100" class="st1 st2">{1}</text>
<text id="XMLID_5_" x="255" y="370" class="st1 st3 middle">{2}</text>
<text id="XMLID_6_" x="255" y="500" class="st1 st4 st7 middle">{3}</text>
<text id="XMLID_7_" x="480" y="595" class="st1 st2 end">{4}</text>
</svg>
"""
radi="""<path id="XMLID_14_" d="M451.9,134.5c-6.3-10.2-26.9-10.4-56.1-2.6c-2.4-8.2-9.9-14.2-18.8-14.2c-10.9,0-19.7,8.8-19.7,19.8
	c0,2.4,0.5,4.6,1.3,6.7c-36.9,14.3-81.3,36.6-127.1,65c-106.5,66-180.4,139.6-165.1,164.3s114.1-8.7,220.6-74.7
	S467.2,159.2,451.9,134.5z M285.8,297.3c-103,63.8-198.6,96.2-213.4,72.3s56.7-95.1,159.7-158.9c46.1-28.5,90.6-50.7,127.1-64.5
	c3.2,6.5,9.9,11,17.6,11c10.9,0,19.7-8.8,19.7-19.8c0-1-0.2-2-0.3-2.9c25.6-6.1,43.5-5.4,49.2,3.9
	C460.4,162.3,388.9,233.5,285.8,297.3z"/>
"""
def solCount(n, x):
    if x == True:
        return '(%s)'%n
    else:
        return '%s'%n

mpp = {True: radi, False: ''}
f = open('input.txt', 'r')
ipt = f.read()
f.close()
lst = ipt.split('\n')
for i in lst:
    if (len(i) < 2): continue
    pls = i.split(' ')
    # print pls
    Mcount = float(pls[-1])
    NAME = pls[-2]
    name = pls[-3]
    id = int(pls[0].split('.')[0])
    if id >= 84 or id == 43:
        ifrad = True
    else:
        ifrad = False
    f = open('output\\%s.%s.svg'%(id, NAME), 'w')
    f.write(comm)
    f.write('\n')
    if (len(NAME) > 8):
        f.write(rstr2.format(mpp[ifrad], id, name, NAME, solCount(Mcount, ifrad)))
    else:
        f.write(rstr1.format(mpp[ifrad], id, name, NAME, solCount(Mcount, ifrad)))
    f.close()
