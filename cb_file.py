from selenium.webdriver import Chrome, ChromeOptions
import time
import re
from bs4 import BeautifulSoup
import requests
import os
from PyPDF2 import PdfFileMerger
 
opt = ChromeOptions()            # 创建Chrome参数对象
opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
driver = Chrome(options=opt)     # 创建Chrome无界面对象

#使用无界面浏览器访问中国经营报电子版
driver.get('http://dianzibao.cb.com.cn/')
time.sleep(5)
first_page = driver.page_source
soup = BeautifulSoup(first_page, "lxml")
driver.close()

#获取网页中pdf文件的相对链接
pdf_str = []
pdfs = soup.find_all('a',{'href':re.compile('\.\.\/\.\.\/\.\.\/images\/.*')})
for pdf in pdfs:
    pdf_str.append(pdf['href'])

#更改相对链接为绝对链接
pdf_urls=[]
for i in pdf_str:
    pdf_urls.append('http://dianzibao.cb.com.cn'+i[8:])
    
#pdf链接去重
l1 = pdf_urls
l2 = list(set(l1))
l2.sort(key=l1.index)
pdf_urls = l2

#pdf下载
dir_name = time.strftime("%Y-%m-%d", time.localtime())
folder = os.path.exists(dir_name)
if not folder:
    os.makedirs(dir_name) 
file_name = 1
for url in pdf_urls:
    responsepdf = requests.get(url)
    full_name = dir_name+'/'+'%d'%file_name + ".pdf"
    print(url)
    print(full_name)
    if responsepdf.status_code == 200:
        with open(full_name,"ab+") as code:
            code.write(responsepdf.content)
            time.sleep(1)  # 防止访问速度过快，可以灵活的调整时间 
        code.close()
    file_name = file_name+1

#pdf文件合并
target_path = dir_name
# pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
# pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

#path = os.listdir(target_path)     # 输入文件夹地址
files = os.listdir(target_path)   # 读入文件夹
num_pdf = len(files)
name_list = [str(name)+".pdf" for name in range(1,num_pdf+1)]
pdf_lst = [os.path.join(target_path, filename) for filename in name_list]


file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)     # 合并pdf文件
file_merger.write(dir_name+".pdf")
print('合并完成')