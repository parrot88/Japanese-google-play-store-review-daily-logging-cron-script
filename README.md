# Japanese-google-play-store-review-daily-logging-cron-script

## Description
This is script get log review count and review average count at Japanese google play store everyday by cron.  
This is only for Japanese application, cause this script analyse web page in Japanese.  
Sorry for English developer.  

## Usage
1. edit your application's URL at Google Play Store with 'do.py'
> googlePlayURL = "https://play.google.com/store/apps/details?id=com.hoge.hoge&hl=ja"

2. set cron and give permission +x into 'do.py'
If you wanna check review at every pm 10, edit cron.
Please edit as below...  
> 0 22 * * * python3 /your/project/path/do.py >> /your/log/path/log.txt  

And don't forget add permission +x to 'do.py'.

4. check result at 'log.txt'  
for example: 

```2020/10/21 21:00:07 9 件, 星平均: 2.6
2020/10/22 21:00:07 10 件, 星平均: 2.4
2020/10/23 21:00:07 10 件, 星平均: 2.4
```
Log format is ... date, review score, review average score

## By the way...
I used this script at my Raspberry Pi zero w.  
That is enough spec.  
It worked Python 3.6.5.  
