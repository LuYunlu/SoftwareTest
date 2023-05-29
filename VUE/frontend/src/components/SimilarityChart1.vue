<template>
  <div class="cluster">
    <div class="echart" id="simichart1" :style="myChartStyle"></div>
  </div>
</template>

<script>
import axios from 'axios';
import * as echarts from "echarts";
//const d3=require('d3-dsv')
export default {
   data(){
      return{
        myChart:{},
        xData:[],
        yData:[],
        yData1:[],
        y1name:'',
        myChartStyle:{float: "left", width: "100%", height: "85%"},
        flag:0
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
        }
    },
    methods:{
        Initdata()
        {
            const path="http://localhost:5000/similar";
            axios.get(path).then(res=>{
                    var v = res.data[0]
                    var v1 = res.data[1]
                    for(var i=0;i<v.length;i++){
                        this.xData.push(String(v[i].Date))
                        this.yData.push(Number(v[i].value))
                        this.yData1.push(Number(v1[i].value))
                        this.flag=1
                    }
                    this.y1name = String(res.data[4][0].value)
            })
            ///console.log(111)
        },
        initEcharts() {
        const option={
          dataZoom: [{
                  type: 'slider',
                  show:true ,
                  xAxisIndex: [0],
                  filterMode: 'filter',
                  bottom: 10
          }],
          legend: {
              data: ["异常曲线-0.csv",'相似度top1: '+this.y1name+'.csv'],
              textStyle: {
                  fontSize: 10, //图例字体大小
              },
              itemHeight: 10,  //图例大小
              type: 'scroll', //图例滚动显示
              orient: 'vertical', //图例纵向显示
              //图例位置
              right: 0,
              top: 30,
              bottom: 30,
          },
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
          series:[
              {
                name: '异常曲线-0.csv',
                data:this.yData,
                type:"line",
                showSymbol:true,
                itemStyle: {
                    borderRadius: 30,
                },
              },
              {
                name: '相似度top1: '+this.y1name+'.csv',
                data:this.yData1,
                type:"line",
                showSymbol:true,
                itemStyle: {
                    borderRadius: 30,
                },
              }
          ],
          color:['#ec0606','#e1aabb'],

          tooltip: {
            trigger: 'axis',
                axisPointer: {
                    type: 'line',
                    label: {
                        backgroundColor: '#fff'
                    }
                }
          },
          grid: { //坐标系设置
            top: 10,
            left: 5,
            right: 30,
            bottom: 50,
            containLabel: true
          }
      }
      
      this.myChart = echarts.init(document.getElementById("simichart1"));
      this.myChart.setOption(option);
      window.addEventListener("resize",()=>{
        this.myChart.resize();
      })
    },

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