<template>
    <div class="node">
      <div class="title1">节点层单指标</div>
    <select v-model="clusterchoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
      @change="ChooseCluster($event)">
      <option value="">请选择所要展示集群</option>
      <option v-for="item in clusterlist" v-bind:key="item.id" v-text="item.name"></option>
    </select>
    <select v-model="nodechoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
      @change="ChooseNode($event)">
      <option value="">请选择所要展示结点</option>
      <option v-for="item in nodelist" v-bind:key="item.id" v-text="item.name"></option>
    </select>
    <select v-model="nodefeature" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
      @change="Choose_Node_Feature($event)">
      <option value="">请选择所要展示结点特征</option>
      <option v-for="item in node_feature_list" v-bind:key="item.id" v-text="item.name"></option>
    </select>
     <div class="echart" id="mychart3" :style="myChartStyle"></div>
  </div>
</template>

<script>
import axios from 'axios';
import * as echarts from "echarts";
//const d3=require('d3-dsv')
export default {
    data(){
    return{
      clusterlist:[{name:"cc-cc408-hya",id:1},{name:"cc-cc553-interestPrice",id:2}],
      nodelist:[{name:"data-node-01",id:1},{name:"data-node-02",id:2},{name:"data-node-03",id:3},{name:"data-node-04",id:4},{name:"data-node-05",id:5},
      {name:"data-node-06",id:6},{name:"data-node-07",id:7},{name:"data-node-08",id:8},{name:"data-node-09",id:9},{name:"data-node-10",id:10},{name:"data-node-11",id:11},
      {name:"data-node-12",id:12},{name:"data-node-13",id:13},{name:"data-node-14",id:14},{name:"data-node-15",id:15},{name:"data-node-16",id:16},{name:"data-node-17",id:17},
      {name:"data-node-18",id:18},{name:"data-node-19",id:19},{name:"data-node-20",id:20},{name:"master-vm-01",id:21},{name:"master-vm-02",id:22},{name:"master-vm-03",id:23}],
      node_feature_list:[{name:"index_time_seconds_total",id:1},{name:"search_query_time_seconds",id:2},{name:"os_load5",id:3},{name:"process_cpu_percent",id:4},
      {name:"transport_rx_size_bytes_total",id:5},{name:"transport_tx_size_bytes_total",id:6}],
      myChart2:{},
      xData2:[],
      yData2:[],
      flag2:0,
      clusterchoose:"cc-cc408-hya",
      nodechoose:"data-node-01",
      nodefeature:"index_time_seconds_total",
      initialized:0,
      myChartStyle:{float:"left", width: "100%", height: "85%"}
      }
    },
    created()
    {
      this.Initdata()
    },
    mounted(){
        this.initEcharts2();
    },
    watch:{
        flag2:function()
    {
      this.flag2=0
      this.initEcharts2();
    },
    initialized:function()
    {
      this.initEcharts2()
    }
    },
    methods:{
         initEcharts2()
    {
      const option={
          dataZoom: [{
                  type: 'slider',
                  show:true ,
                  xAxisIndex: [0],
                  filterMode: 'filter',
                  bottom: 10
          }],
          xAxis:[{
            data: this.xData2,
            type: 'category',
            boundaryGap: false,
            axisLabel: {
                color: '#000',
                fontSize: 12
            }
          }],
          yAxis:[{
                type: 'value',
                axisLabel: {
                    color: '#000',
                    fontSize: 16
                },
                axisLine: {
                    show: true
                },
                axisTick: {
                    show: true
                },
                // 网格颜色
                splitLine: {
                    lineStyle: {
                        color: '#000',
                        opacity: 0.5
                    }
                },
                min: (value) => {
                    return value.min
                },
                max: (value) => {
                    return value.max
                }
            }],
          series:[{
              data:this.yData2,
              type:"line",
              showSymbol:false,
              itemStyle: {
                  borderRadius: 30,
                },
          }],
          color: ["rgba(21,75,200,0.9)"],

          tooltip: {
            trigger: 'axis',
                axisPointer: {
                    type: 'line',
                }
          },
          grid: {
            //坐标系设置
            top: 10,
            left: 5,
            right: 30,
            bottom: 50,
            containLabel: true
          }
      }

      this.myChart2 = echarts.init(document.getElementById("mychart3"));
      this.myChart2.setOption(option);
      window.addEventListener("resize",()=>{
        this.myChart2.resize();
      })
    },

   ChooseCluster(event)
    {
      this.clusterchoose=event.target.value
      if(this.nodefeature!=""&&this.nodechoose!=""){
              this.ChangeNodedata()
      }
    },
    ChooseNode(event)
    {
      this.nodechoose=event.target.value
      if(this.nodefeature!=""&&this.clusterchoose!=""){
              this.ChangeNodedata()
      }

    },
    Choose_Node_Feature(event)
    {
      this.nodefeature=event.target.value
      if(this.clusterchoose!=""&&this.nodechoose!=""){
              this.ChangeNodedata()
      }

    },
    Initdata:function()
    {
        const path='http://localhost:5000/nodeinfo1';
        axios.get(path,{
             params:{
                cluster_name:this.clusterchoose,
                node_name:this.nodechoose,
                feature:this.nodefeature
            },
        }).then(res=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData2.push(String(this.value[i].Date))
                    this.yData2.push(Number(this.value[i].value))
                }
                this.initialized=1
        })
    },
    ChangeNodedata:function()
    {
      this.xData2=[]
      this.yData2=[]
      const path='http://localhost:5000/nodeinfo1';
        axios.get(path,{
             params:{
                cluster_name:this.clusterchoose,
                node_name:this.nodechoose,
                feature:this.nodefeature
            },
        }).then(res=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData2.push(String(this.value[i].Date))
                    this.yData2.push(Number(this.value[i].value))
                    this.flag2=1
                }
        })
    }
    }
}
</script>
<style>
.node{
    height:100%
}

</style>