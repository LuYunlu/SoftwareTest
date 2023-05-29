<template>
<div id="warn">
        <select v-model="clusterchoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
          @change="ChooseCluster($event)">
          <option v-for="item in clusterlist" v-bind:key="item.id" v-text="item.name"></option>
        </select>
        <input class="text"  v-model.trim="value" style="width:100px;height:25px;margin-top:5px;margin-bottom:5px;margin-left:10px" placeholder="请输入阈值">
    <button type="submit"  @click ="search" style="width:50px;height:25px;margin-top:5px;margin-bottom:5px;margin-left:10px">查询</button>
    <div class="box1">
        <textarea v-model="datainfo" cols="140" rows="20"></textarea>
    </div>

</div>
</template>

<script>
import axios from "axios"
export default {
  data(){
    return{
      clusterlist:[{name:"cc-cc408-hya",id:1},{name:"cc-cc553-interestPrice",id:2}],
      value:"",
      clusterchoose:"cc-cc408-hya",
    };
  },
    mounted() {
  },

  methods:{
    ChooseCluster(event)
    {
      this.clusterchoose=event.target.value
    },
    search:function()
    {
       const path="http://localhost:5000/warn"
      axios.get(path,{
        params:{
            cluster_name:this.clusterchoose,
            value:this.value,
        }
      }).then(res=>{
            this.datainfo=res.data
            this.$forceUpdate()
      })
   },


  }
};
</script>

