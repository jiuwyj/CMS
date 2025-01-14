# 项目说明

---

## 1. 返回页面二全部信息：

1. 对应函数：get_page2_data
2. 输入：查询语句
3. 返回类型：字典

> 格式：
> ``` 
>   {'count':{'fofa':99,...},
>    'data':[{'ip':'1.1.1.1', ...},...],
>    'rank':{'protocol':[{'count':11,'name':'http'}...],...}
>    'truth':{{'fofa':0.99, 'zoomeye':0.98...}}}
> ```
> 具体可参考main.py文件中的page_2变量

## 2. 返回页面三的全部信息：

1. 对应函数：get_page3_data
2. 输入：查询语句
3. 返回类型：字典

> 格式：
> ```
> { 'data': [{'ip':'1.1.1.1', ...},...],
>     'truth_sum': 0.98
> }
> ```
> 具体可参考main.py文件中的page_3变量

# 注意事项

---

1. 为保证项目的完整性与准确性，请以项目形式打开该文件夹，并设置python解释器，如需修改建议在该文件内进行修改
2. 在使用pythonfofa模块时请先修改client.py的Client类中的self.url为https://fofa.red/api/v1，若是打算使用自己的email和key则使用原url
3. 因增加数据条数的功能需要修改zoomeye.sdk内容，第234行return dork_data--->return all_data
4. 在使用truth_for_website函数（获取五个测绘引擎置信度）时，请确保已存在/data/out.xlsx文件（计算置信度结果文件），
如果没有请放入训练文件（/data/2000_all.xlsx），并设置flag为True进行训练
5. detail_init.txt、detail_init_3.txt、detail_to.txt仅为数据测试，与代码无关
6. 代码中测试注释可根据需要进行删除