#This is a small program in the url dowmload video
#This crawler is invalid because it has not been updataed for a long time
#But this  program shows some rudimentary proxy usage and anti-leech
import requests#To the specific library fenction
Url= "https://www.pearvideo.com/video_1742141"#This the target url
ContId=Url.split("_")[1]#Back the "_" is the anti-leech(So we need to cut "1742141" down)
videoStatusurl=f"https://www.pearvideo.com/videoStatus.jsp?contId={ContId}"#Link the chain whith the video site
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                 " AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/107.0.0.0 Safari/537.36",

    "Referer":"https://www.pearvideo.com/video_1742141"#The level above the current request
}#We need to disguise the program like a normal browser access
proxies={
    "https":"https://60.211.218.78:53281"
}#Using a proxy


resp=requests.get(videoStatusurl,headers=headers,proxies=proxies)#Obtain web source code
#print(resp.json())#Check whether the file is successfully obtained
#Failed,but verified not caused by cookie
dic=resp.json()#Plug the code into a dictionary
srcUrl=dic['videoInfo']['videos']['srcUrl']#Find the location of the video
#Grab packet through NetWork and find file inside srcUrl in videos in videoInfo
systime=dic['systemTime']#The time in the Url
srcUrl=srcUrl.replace(systime,f"cont-{ContId}")#Splice the video with the specific location,which is the contid we prepared
print(srcUrl)#verify success
#https://video.pearvideo.com/mp4/adshort/20210919/cont-1742141-15771006_adpkg-ad_hd.mp4
#https://video.pearvideo.com/mp4/adshort/20210919/1669783396705-15771006_adpkg-ad_hd.mp4
#https://video.pearvideo.com/mp4/adshort/20210919/1669784592728-15771006_adpkg-ad_hd.mp4
with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)#Download Video
