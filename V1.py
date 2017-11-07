from __future__ import print_function
from selenium import webdriver
import datetime

set_hour =0;
set_minute = 0;
set_second = 0;

set_hour = input("input hour:")
set_minute = input("input minute:")
set_second = input("input second:")

browser = webdriver.Chrome()





browser.get("http://www.insight-china.cn/conference/MiniSite/AttendUser/MyTicket?CId=426&SId=721")


while True:
	i = datetime.datetime.now()

	if  i.hour==set_hour and i.minute==set_minute and i.second==set_second:
		print("time out")
		browser.get("http://www.insight-china.cn/conference/MiniSite/AttendUser/MyTicket?CId=426&SId=721")
		print("Whether Continue?  1/0")
		choice = input("input there:")
		if choice==1:
			set_hour = input("input hour:")
			set_minute = input("input minute:")
			set_second = input("input second:")
			continue
		else:
			break
	else:
		print("wait",i.minute)
else:
	print("Please check the WEB details......")
	browser.quit()
		
#填充表单		
#setword = browser.find_element_by_id('kw').clear() #表单id = kw
#setword.send_keys(("开始秒杀").decode('GB2312'))  #进行中文转Unicode

#linkElem = browser.find_element_by_id('su').click() #submit  id = su，并执行click