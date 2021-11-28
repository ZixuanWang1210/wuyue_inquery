import os
import re
import webbrowser

s1 = "http://app.wylkyj.com/ExamAPI/Exam/Marking/ScorePicOSS?exam_no=38189&e_dbname=exam_38189&stu_no=100118"
s2 = "&esub_no=38189"
s3 = "&subjectPage=2&isshow=1"
print ("说明：\n 1.本程序仅可免费查询此次联考答题卡\n 2.查询内容包括：答题卡扫描版、小题得分、作文双评分别得分、阅卷教师和阅卷时间\n 3.图像可右键下载保存，使用浏览器查看时可使用缩放功能进行缩放\n 4.本程序仅限个人使用，禁止拷贝\n 5.输入完成以回车结束\n\n\n")
stu = input("请输入准考证号后四位  ")
print("\n查询语文 01\n查询数学 03\n查询英语 04\n查询理综 05\n")

sub = input("请输入查询学科  ")
url = s1 + stu + s2 + sub + s3
temp = int(sub)
if int(sub) == 0:
    for num in range(1,7):
        if num == 2 or num == 5:
            continue
        else:
            url = s1 + stu + s2 + str(num) + s3
            webbrowser.open(url, new=0, autoraise=True)

else:
    print(url)
    webbrowser.open(url, new=0, autoraise=True)
