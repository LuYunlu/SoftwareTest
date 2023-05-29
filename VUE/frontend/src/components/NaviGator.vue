<template>
  <nav>
    <router-link to="/">大数据集群监控</router-link> |
    <router-link to="/similar">波动相似性对比</router-link>|
    <router-link to="/warning">警告页面</router-link>
  </nav>
</template>

<script>
export default {
    
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
}

nav {
  position: relative;
  padding: 20px;
  margin-left: 28%;
  width: 350px;
  height: 30px;
  size: 500px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
