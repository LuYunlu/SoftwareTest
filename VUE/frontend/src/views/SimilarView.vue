<template>
  <div class="gross">
    <div class="NG">
      <Navigator></Navigator>
    </div>
    <div class="Similarity1">
      <Similarity1 ref="similarity1"></Similarity1>
    </div>
    <div class="Similarity2">
      <Similarity2 ref="similarity2"></Similarity2>
    </div>
    <div class="Similarity3">
      <Similarity3 ref="similarity3"></Similarity3>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import Navigator from "@/components/NaviGator.vue";
import Similarity1 from "@/components/SimilarityChart1.vue";
import Similarity2 from "@/components/SimilarityChart2.vue";
import Similarity3 from "@/components/SimilarityChart3.vue";
export default {
    name: 'SimilarView',
    components:{
        Similarity1,
        Similarity2,
        Similarity3,
        Navigator
    }
    // mounted() {
    //     this.loading=true
    //     this.initialData()
    //     console.log(this.content)
    // },
    // methods: {
    //     initialData:function(){
    //         axios.get("http://localhost:5000/similar").then(res=>{
    //             // this.content=res.data[0]
    //             // this.loading=false
    //         })
    //         .catch(err=>{
    //             // this.content = []
    //             console.log(err)
    //         })
    //     }
    // },
}
</script>

<style>
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
.container{
  position:relative;
  left:0px;
  top:0px;
  width:100vw;
  height:100vh;
}
.back{
  position:absolute;
  z-index:-1;
  width:100%;
  height:1615px;
  left:0px;
  top:0px;
}
.Similarity1{
  position:absolute;
  left:4%;
  height:500px;
  top:90px;
  width:80%;
}
.Similarity2{
  position:absolute;
  left:4%;
  top:600px;
  width:80%;
  height:500px;
}
.Similarity3{
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