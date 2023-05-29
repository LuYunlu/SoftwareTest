# 大数据集群监控和异常定位
#### 监控数据展示： 集群层面、单节点层面、多节点层面
#### 波动相似性对比：ranked top 1~3

## 部署：

### 后端：  
#### pip install flask  
#### pip install Flask-Cors  
#### pip install flask_sqlalchemy
### 后端运行：
```
python app.py;
```

### 前端：   
#### npm install axios   
#### npm install echarts   
#### npm install element-plus
### 前端运行：
#### 进入VUE/frontend目录下：
```
yarn install
yarn serve
```


## 使用说明：   
共有三个页面:大数据集群监控、波动相似性对比分析、以及警告页面

大数据集群监控页面：   
集群、单节点、多节点层面各一个折线图，下拉框可以选择不同集群不同节点以及不同指标。      

相似度对比分析页面：
展示了相似度排名前1~3的折线图，折线数量随排名降低而递增

警告页面：
通过下拉框选择不同集群，并输入指定阈值，将返回该集群中超出此阈值的数据。

每张图底部有可以压缩查看时间的拖动栏


## 接口说明
### clusterinfo
#### 接口功能
> 展示集群层面的信息
#### URL
> http://localhost:5000/clusterinfo
#### HTTP请求方式
> GET
#### 请求参数
|参数|必选|类型|说明|
|----- |-------|-----|-----|
|cluster_name|ture|string|请求的集群名|
|feature    |true    |string   |请求的特征名|
#### 返回字段
|返回字段|字段类型| 说明                  |
|-----|------|---------------------|
|value  |json   | [Date，value]的二元数组列表 |
#### 接口示例
> 地址：[http://localhost:5000/clusterinfo?cluster_name='cc-cc408-hya'&feature='active_shards']
``` javascript
[
    {"Date": xxx,"value": xxx},
    {"Date": xxx,"value": xxx},...
]
```
### nodeinfo1
#### 接口功能
> 展示单节点层面的信息
#### URL
> http://localhost:5000/nodeinfo1
#### HTTP请求方式
> GET
#### 请求参数
|参数|必选|类型|说明|
|-----  |-------|-----|-----                               |
|cluster_name    |ture    |string|请求的集群名                          |
|node_name    |true    |string   |请求的节点名|
|feature    |true    |string   |请求的特征名|
#### 返回字段
|返回字段|字段类型| 说明                  |
|----   |------|---------------------|
|value  |json   | [date，value]的二元数组列表 |
#### 接口示例
> 地址：[http://localhost:5000/nodeinfo1?cluster_name='cc-cc408-hya'&node_name=data-node-04&feature='process_cpu_percent']
``` javascript
[
    {"date": xxx,"value": xxx},
    {"date": xxx,"value": xxx},...
]
```
### nodeinfo2
#### 接口功能
> 展示多节点层面的信息
#### URL
> http://localhost:5000/nodeinfo2
#### HTTP请求方式
> GET
#### 请求参数
|参数|必选|类型|说明|
|-----  |-------|-----|-----                               |
|cluster_name    |ture    |string|请求的集群名                          |
|node_name    |true    |string   |请求的节点名|
|mount_name    |true    |string   |请求的磁盘名|
#### 返回字段
| 返回字段  | 字段类型 | 说明                  |
|-------|------|---------------------|
| value | json | [date，value]的二元数组列表 | 
#### 接口示例
> 地址：
[http://localhost:5000/nodeinfo2?cluster_name='cc-cc408-hya'&node_name='data-node-04'&mount_name='/srv/data01 (/dev/sdb)']
``` javascript
[
    {"date": xxx,"value": xxx},
    {"date": xxx,"value": xxx},...
]
```



