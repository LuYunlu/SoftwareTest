<template>
<div class="gross">
  <div class="NG">
    <Navigator></Navigator>
  </div>
  <div class="Cluster">
    <ClusterChart ref="clusterchart"></ClusterChart>
  </div>
  <div class="NodeChart">
    <NodeChart ref="nodechart"></NodeChart>
  </div>
  <div class="Multinode">
    <MultiNode ref="multinode"></MultiNode>
  </div>


</div>
</template>

<script>

import ClusterChart from "@/components/ClusterChart.vue";
import NodeChart from "@/components/NodeChart.vue";
import MultiNode from "@/components/MultiNode.vue";
import Navigator from "@/components/NaviGator.vue";

export default {
  components:{
    ClusterChart,
    NodeChart,
    MultiNode,
    Navigator,
  },
  methods:{
    // 刷新
   flush()
   {
    console.log(1111)
    this.$refs.clusterchart.Changedata()
    this.$refs.nodechart.ChangeNodedata()
    this.$refs.multinode.Changedata()
   }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.gross{
  position:relative;
  left:0px;
  top:0px;
  width:100vw;
  height:100vh;
}

.Cluster{
  position:absolute;
  left:4%;
  height:500px;
  top:90px;
  width:80%;
}
.NodeChart{
  position:absolute;
  left:4%;
  top:600px;
  width:80%;
  height:500px;
 
}
.Multinode{
  position:absolute;
  left:4%;
  top:1100px;
  width:80%;
  height:500px
}
.NG
{
  position:absolute;
  top:10px;
  height:30px;
  width:100%;

}
</style>
