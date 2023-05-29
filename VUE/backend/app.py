import numpy as np
from flask import Flask, render_template, request, Response, redirect, jsonify, json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from hashlib import md5
import pandas as pd
import sqlite3

from VUE.backend import similarity

app = Flask(__name__,static_folder='../frontend/dist',template_folder="../frontend/dist",
            static_url_path="")
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)

conn = sqlite3.connect('data.db', check_same_thread=False)


@app.route('/clusterinfo', methods=['GET'])
def get_cluster_feature():
    cluster_name = request.args.get('cluster_name')
    feature = request.args.get('feature')
    values = pd.read_sql_query(
        "select Date,value from cluster where cluster_name='" + cluster_name + "' and metric_name='" + feature + "';", conn)
    values = values.to_dict('records')
    return jsonify(values)


@app.route('/nodeinfo1', methods=['GET'])
def nodeinfo():
    cluster_name = request.args.get('cluster_name')
    node_name = request.args.get('node_name')
    feature = request.args.get('feature')
    values = pd.read_sql_query(
        "select Date,value from '" + feature + "' where cluster_name='" + cluster_name + "' and node_name='" + node_name + "';",
        conn)
    values = values.to_dict('records')
    return jsonify(values)


# ----node info 2(mount) 多节点----
@app.route('/nodeinfo2', methods=['GET'])
def nodeinfo2():
    cluster_name = request.args.get('cluster_name')
    node_name = request.args.get('node_name')
    mount_name = request.args.get('mount_name')
    values = pd.read_sql_query(
        "select Date,value from bytes where cluster_name='" + cluster_name + "' and mount='" + mount_name + "' and node_name='" + node_name + "';",
        conn)
    values = values.to_dict('records')
    return jsonify(values)


@app.route('/similar', methods=['GET'])
def showsimilarity():
    calcutable = 'similar2'
    drawtable = 'similar2'
    # 提取value值
    selectvalues = []
    for i in range(21):
        tempvalues = (
            np.array(
                pd.read_sql_query('select value from ' + calcutable + ' where "group"=' + str(i) + ';',
                                  conn))).flatten()
        tempvalues = tempvalues.tolist()
        selectvalues.append(tempvalues)
    nameofrank1, nameofrank2, nameofrank3 = similarity.calsimilarity(selectvalues)
    # normalization.normal(selectvalues)

    csv0 = pd.read_sql_query('select Date,value from ' + drawtable + ' where "group"=0;', conn)
    csv0 = csv0.to_dict('records')
    rank1 = pd.read_sql_query('select Date,value from ' + drawtable + ' where "group"=' + str(nameofrank1) + ';', conn)
    rank1 = rank1.to_dict('records')
    rank2 = pd.read_sql_query('select Date,value from ' + drawtable + ' where "group"=' + str(nameofrank2) + ';', conn)
    rank2 = rank2.to_dict('records')
    rank3 = pd.read_sql_query('select Date,value from ' + drawtable + ' where "group"=' + str(nameofrank3) + ';', conn)
    rank3 = rank3.to_dict('records')
    values = []
    values.append(csv0)
    values.append(rank1)
    values.append(rank2)
    values.append(rank3)  # print(rank1)# print(rank2)# print(rank3)
    rank = []
    rank.append({'rank': '1', 'value': nameofrank1})
    rank.append({'rank': '2', 'value': nameofrank2})
    rank.append({'rank': '3', 'value': nameofrank3})
    print(rank)
    values.append(rank)
    return jsonify(values)

# warning
@app.route('/warn', methods=['GET'])
def warn():
    cluster_name = request.args.get('cluster_name')
    value = request.args.get('value')
    values = []
    res = ""
    res += "节点层多指标\n"
    values = (pd.read_sql_query(
        "select node_name,mount,Date,value from bytes where cluster_name='" + cluster_name + "' and value >'" + value + "';",
        conn)).to_dict('records')
    for i in values:
        res += "节点为"+str(i['node_name'])+"，"+"磁盘为"+str(i['mount'])+"，在"+str(i['date'])+"时刻，其值为"+str(i['value'])+'超出给定阈值\n'
    res += '\n'
    res += "集群层面\n"
    values = (pd.read_sql_query(
        "select Date,value from cluster where cluster_name='" + cluster_name + "' and value >'" + value + "';",
        conn)).to_dict('records')
    for i in values:
        res += "在"+str(i['Date'])+"时刻，其值为"+str(i['value'])+'超出给定阈值\n'
    res += '\n'
    res += "节点层单指标\n"
    res += "index_time_seconds_total特征\n"
    values = (pd.read_sql_query(
        "select node_name,Date, value from index_time_seconds_total where cluster_name='" + cluster_name + "' and value >'" + value + "';",
        conn)).to_dict('records')
    for i in values:
        res += "节点为"+str(i['node_name'])+"，在"+str(i['Date'])+"时刻，其值为"+str(i['value'])+'超出给定阈值\n'
    res += '\n'
    res += "os_load5特征\n"
    values = (pd.read_sql_query(
        "select node_name,Date,value from os_load5 where cluster_name='" + cluster_name + "' and value >'" + value + "';",
        conn)).to_dict('records')
    for i in values:
        res += "节点为" + str(i['node_name']) + "，在" + str(i['Date']) + "时刻，其值为" + str(i['value']) + '超出给定阈值\n'
    res += '\n'
    res += "process_cpu_percent特征\n"
    values = (pd.read_sql_query(
        "select node_name,Date,value from process_cpu_percent where cluster_name='" + cluster_name + "' and value >'" + value + "';",
        conn)).to_dict('records')
    for i in values:
        res += "节点为" + str(i['node_name']) + "，在" + str(i['Date']) + "时刻，其值为" + str(i['value']) + '超出给定阈值\n'
    res += '\n'
    res += "search_query_time_seconds特征\n"
    values = (pd.read_sql_query(
        "select node_name,Date,value from search_query_time_seconds where cluster_name='" + cluster_name + "' and value >'" + value + "';",
        conn)).to_dict('records')
    for i in values:
        res += "节点为" + str(i['node_name']) + "，在" + str(i['Date']) + "时刻，其值为" + str(i['value']) + '超出给定阈值\n'
    res += '\n'
    res += "transport_rx_size_bytes_total特征\n"
    values = (pd.read_sql_query(
        "select node_name,Date,value from transport_rx_size_bytes_total where cluster_name='" + cluster_name + "' and value >'" + value + "';",
        conn)).to_dict('records')
    for i in values:
        res += "节点为" + str(i['node_name']) + "，在" + str(i['Date']) + "时刻，其值为" + str(i['value']) + '超出给定阈值\n'
    res += '\n'
    res += "transport_tx_size_bytes_total特征\n"
    values = (pd.read_sql_query(
        "select node_name,Date,value from transport_tx_size_bytes_total where cluster_name='" + cluster_name + "' and value >'" + value + "';",
        conn)).to_dict('records')
    for i in values:
        res += "节点为" + str(i['node_name']) + "，在" + str(i['Date']) + "时刻，其值为" + str(i['value']) + '超出给定阈值\n'

    return res

@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
