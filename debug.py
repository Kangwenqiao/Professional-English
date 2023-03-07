# coding=gbk
import requests
url="https://www.pearvideo.com/video_1742141"
contid=url.split("_")[1]
videoStatusurl=f"https://www.pearvideo.com/videoStatus.jsp?contId={contid}"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                 " AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/107.0.0.0 Safari/537.36",

    "Referer":"https://www.pearvideo.com/video_1742141"
}


resp=requests.get(videoStatusurl,headers=headers)
#print(resp.json())
dic=resp.json()
srcUrl=dic['videoInfo']['videos']['srcUrl']
systime=dic['systemTime']
srcUrl=srcUrl.replace(systime,f"cont-{contid}")
print(srcUrl)
#https://video.pearvideo.com/mp4/adshort/20210919/cont-1742141-15771006_adpkg-ad_hd.mp4
#https://video.pearvideo.com/mp4/adshort/20210919/1669783396705-15771006_adpkg-ad_hd.mp4
#https://video.pearvideo.com/mp4/adshort/20210919/1669784592728-15771006_adpkg-ad_hd.mp4


with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)
