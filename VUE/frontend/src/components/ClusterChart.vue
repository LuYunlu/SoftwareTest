<template>
    <div class="cluster">
        <div class="title1">集群层面</div> 
<select v-model="clusterchoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
            @change="ChooseCluster($event)">
  <option v-for="item in clusterlist" v-bind:key="item.id" v-text="item.name"></option>
</select>
       
<select v-model="featurechoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
          @change="ChooseFeature($event)">
  <option v-for="item in featurelist" v-text="item.name" v-bind:key="item.id"></option>
  </select>
       
  <div class="echart" id="mychart" :style="myChartStyle"></div>
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
        featurelist:[{name:"active_shards",id:1},{name:"number_of_nodes",id:2},{name:"status",id:3}],
        myChart:{},
        xData:[],
        yData:[],
        myChartStyle:{float: "left", width: "100%", height: "85%"},
        flag:0,
        clusterchoose:"cc-cc408-hya",
        featurechoose:"active_shards",
        initialized:0
      }
   },
    created() {
       this.Initdata()
    },
    mounted() {
        this.initEcharts()
    },
    watch:{
        flag:function() {
          this.flag=0
          this.initEcharts();
        },
        initialized:function() {
          this.initEcharts()
        }
    },
    methods:{
        initEcharts() {
        const option={
          dataZoom: [{
                  type: 'slider',
                  show:true ,
                  xAxisIndex: [0],
                  filterMode: 'filter',
                  bottom: 10
          }],
          xAxis:[{
            data: this.xData,
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
              data:this.yData,
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
      
      this.myChart = echarts.init(document.getElementById("mychart"));
      this.myChart.setOption(option);
      window.addEventListener("resize",()=>{
        this.myChart.resize();
      })
    },
     ChooseCluster(event) {
        this.clusterchoose=event.target.value
        if(this.featurename!="")
        {
          this.Changedata()
        }
    },
    ChooseFeature(event) {
      this.featurechoose=event.target.value
      this.Changedata()
    },
    Initdata()
    {
        const path='http://localhost:5000/clusterinfo';
        axios.get(path,{
             params:{
                cluster_name:this.clusterchoose,
                feature:this.featurechoose
            },
        }).then(res=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData.push(String(this.value[i].Date))
                    this.yData.push(Number(this.value[i].value))
                    this.initialized=1
                }
        })
        ///console.log(11111)
    },
    Changedata:function()
    {
        this.xData=[]
        this.yData=[]
        const path='http://localhost:5000/clusterinfo';
        axios.get(path,{
             params:{
                cluster_name:this.clusterchoose,
                feature:this.featurechoose
            },
        }).then(res=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData.push(String(this.value[i].Date))
                    this.yData.push(Number(this.value[i].value))
                    this.flag=1
                }
            })
    }
   }
}

</script>

<style>
.cluster{
    height:100%;
}

select{
  background-color: rgba(1,1,1,0);
  color: rgb(57, 122, 179);
  border-color: rgba(21,75,140,0.5);
  border-radius: 50px;
}
</style>