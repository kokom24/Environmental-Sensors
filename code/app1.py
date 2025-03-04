import try1
import shutil
import os
import time

try1.my_init()

while True:
    temp, hum, pres, gas= try1.my_get()
    print("Result:",temp,hum,pres,gas)

    f = open('index.html', 'w')

    datalist = ['<html>\n']
    f.writelines(datalist)
    datalist = ['<head>\n']
    f.writelines(datalist)
    datalist = ['        <meta charset="utf-8">\n']
    f.writelines(datalist)
    datalist = ['        <meta http-equiv="refresh" content="1;url=index.html">\n']
    f.writelines(datalist)
    datalist = [' <link rel="stylesheet" type="text/css" href="css/style.css">']
    f.writelines(datalist)    
    
    datalist = ['<title>\n']
    f.writelines(datalist)
    text = "特別講義_木村研究室<br>\n"
    result = text
    f.writelines(result)
    datalist = ['</title>\n']
    f.writelines(datalist)
    
    datalist = ['</head>\n']
    f.writelines(datalist)
    datalist = ['<body>\n']
    f.writelines(datalist)
    
    datalist = ['<h1>\n']
    f.writelines(datalist)
    text = "宇宙居住を見据えた小型無線ネットワーク環境センサの開発<br>\n"
    result = text
    f.writelines(result)
    datalist = ['</h1>\n']
    f.writelines(datalist)
    datalist = ['<h3>\n']
    f.writelines(datalist)
    datalist = ['<div style="text-align:right;">']
    f.writelines(datalist)
    text = "齊 藤 龍 輝,　 鈴 木 陸 穏,　 津 曲 花 央,　 小 松 晃 也<br>\n"
    result = text
    f.writelines(result)
    datalist = ['</div>']
    f.writelines(datalist)
    datalist = ['</h3>\n']
    f.writelines(datalist)

    datalist = ['<div style="text-align:center;">']
    f.writelines(datalist)
    datalist = ['<div style="font-size: 3em">']
    f.writelines(datalist)
    datalist = ['<div style="border: 7px solid #cd5c5c; border-radius:10px; padding:5px;">']
    f.writelines(datalist)

    text = "温 度 : {0} 度<br>\n"
    result = text.format(temp)
    f.writelines(result)
    text = "湿 度 : {0} % <br>\n"
    result = text.format(hum)
    f.writelines(result)
    text = "気 圧 : {0} hPa<br>\n"
    result = text.format(pres)
    f.writelines(result)
    text = "ガ ス : {0} ohm <br>\n"
    result = text.format(gas)
    f.writelines(result)
    datalist = ['</div>']
    f.writelines(datalist)    
    
    #datalist = ['<input style=\"width:200px;height:100px; font-size: 200%;\" type=\"button\" value=\"更新\" onclick=\"location.reload()\">\n']
    #f.writelines(datalist)
    datalist = ['</body>\n']
    f.writelines(datalist)
    datalist = ['</html>\n']
    f.writelines(datalist)

    f.close()
    
    shutil.copy2("./index.html", "/var/www/html/index.html")
    
    time.sleep(1)
