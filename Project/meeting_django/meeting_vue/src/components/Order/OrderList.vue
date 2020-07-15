<template>
  <div class="OrderList" v-loading="loading">
    <el-card class="card-content" v-for="dat in orderList" :key="dat.name">
      <div slot="header" class="card-header-text">
        <span style="font-size: 18px; font-weight: bolder">{{ dat.date }}</span>
        <div style="float: right; font-size: 5px"> {{ dat.strTime }} -- {{ dat.endTime }} </div>
      </div>
      <div>
        <span style="font-size: 10px">{{ dat.content }}</span>
      </div>
    </el-card>
    <div class="block">
    <span class="demonstration"></span>
    <el-date-picker
      v-model="date"
      align="right"
      type="date"
      placeholder="选择日期"
      :picker-options="pickerOptions">
    </el-date-picker>
  </div>
  </div>
</template>

<script>
export default {
  name: 'OrderList',
  data () {
    return {
      orderList: null,
      loading: true,
      date: '',
      pickerOptions: {
        disabledDate (time) {
          return time.getTime() > Date.now()
        }
      }
    }
  }
}
</script>
<style scoped>
.card-content {
  min-width: 250px;
  max-width: 550px;
  margin: auto;
  margin-bottom: 20px;
}

.card-header-text {
  height: 8px;
}

.card-header-text span {
  font-size: 9px;
  color: #909399;
}

</style>
