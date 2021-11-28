# 五岳教育双评分查询，答题卡图像查询

# 本项目已不再维护，禁止商用盈利

## step 1 准备

1. 安装python
2. 安装依赖库

## step 2 获取考试编号

1. 找任意一名老师，获得其账号密码（老师一般都会给）
2. 使用老师账号登录阅卷平台，点击成绩查询，选择想要查询的考试
3. 使用抓包工具，对该页面进行抓包
4. 在返回的json文件中，得到`exam_no`后的数值即为考试的ID

### step 3 修改main.py

1. 修改第5行中的`exam_no=`和`e_dbname=exam_`后为刚才查询到的ID

2. ```
   http://app.wylkyj.com/ExamAPI/Exam/Marking/ScorePicOSS?exam_no=*****&e_dbname=exam_*****&stu_no=*****&esub_no=*******&subjectPage=2&isshow=0
   考试ID---------考试名称-------------考号---------------学科编号（考试ID+学科代码0~10）---展示详细信息
   ```

   

## step 4 运行

![b904f1de536fa0f118f6a423f82f6b6](https://i.loli.net/2021/11/28/Vk7GEWaJBmYnH1v.jpg)



效果如图所示

可查询评卷时间、评卷人、作文双评得分等信息
