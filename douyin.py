
import requests
import re

#http请求
def request(url):
	header={"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
	r=requests.get(url,headers=header)
	return r.content

##得到sharetitle
#def gettitle(r):
#	r=r.decode("utf-8")
#	title=str(re.findall(r"shareTitle\".*?\"(.*?)\"",r))
#	title=title.replace("'",'').replace('[','').replace(']','').replace(" ",'').replace("\n",'')
#	return title

#得到视频的itemId和dytk
def getkeys(r):
	i=re.findall(r"itemId.*?\"(.*?)\"",str(r))[0]
	print(i)
	d=re.findall(r"dytk.*?\"(.*?)\"",str(r))[0]
	print(d)
	return i,d


#得到视频id
def getid(url):
	r=request(url)
	id=re.findall(r"uri\":\"(\w{32})\"",str(r))[0]
	return id
	

#保存视频
def savevideo(url,title):
	video=request(url)
	with open(str(title)+".mp4",'wb') as f:
		f.write(video)
		return 1


if __name__=="__main__":
	print("欢迎使用抖音无水印下载工具 by公众号：教程姬")
	shareurl0="https://v.douyin.com/"
	shareid=input("请粘贴抖音分享链接：")
	shareid=re.findall(r"douyin.com\/(.{6})",shareid)
	shareurl=shareurl0+shareid[0]
	print("将要获取的链接为：",shareurl)
	#no.1
	playhtml=request(shareurl)
	itemid,dytk=getkeys(playhtml)
	videourl0="https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/"
	videourl=videourl0+"?item_ids="+str(itemid)+"&dytk="+str(dytk)
	#title=gettitle(playhtml)
	videoid=getid(videourl)
	print(videoid)
	downldurl="https://aweme.snssdk.com/aweme/v1/play/?video_id="+str(videoid)+"&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&is_support_h265=0&source=PackSourceEnum_PUBLISH"
	print("复制下面链接也可以直接下载：\n",downldurl)
	title=str(input("请输入视频名字："))
	ifsave=savevideo(downldurl,title)
	if ifsave:
		print("成功保存视频："+title+".mp4")

	input("按回车结束！")


