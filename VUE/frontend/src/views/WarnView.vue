<template>
<div class="warn">
  <div class="NG">
    <Navigator></Navigator>
  </div>
  <div class="Cluster">
    <ClusterChart ref="clusterchart"></ClusterChart>
  </div>


</div>
</template>

<script>

import ClusterChart from "@/components/WarnPage.vue";
import Navigator from "@/components/NaviGator.vue";

export default {
  components:{
    ClusterChart,
    Navigator,
  },
  methods:{
   flush()
   {
    console.log(1111)
    this.$refs.clusterchart.Changedata()
   }
  }
}
</script>

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
.warn{
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
.NG
{
  position:absolute;
  top:10px;
  height:30px;
  width:100%;

}
</style>
