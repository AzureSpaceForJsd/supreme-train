<template>
<div class="MeetingTime">
  <div id="app">
    <MeetingReserve msg="Welcome to MeetingRoom Reserve System"/>
  </div>
</div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import MeetingReserve from './components/MeetingReserve.vue'

export default {
  name: 'App',
  components: {
    MeetingReserve
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  /* background-image: url("./assets/img/bg.jpg"); */
  background-repeat: no-repeat;
  width: 100%;
  height: 100px;
  background-size: cover;
}
</style>
