<template>
<div>
  <div style="width:100%;text-align:center">
    <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="会议室 " label-width="80px" label-position="center">
      <el-col :span="10">
        <el-select v-model="value" placeholder="请选择会议室">
          <el-option
            v-for="room in rooms"
            :key="room.roomNo"
            :label="room.roomName"
            :value="room.roomName">
          </el-option>
        </el-select>
      </el-col>
    </el-form-item>
    <el-form-item label="预定日期">
      <el-col :span="11">
        <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 50%;"></el-date-picker>
      </el-col>
    </el-form-item>
    <el-form-item label="预定时间">
      <el-col :span="11">
        <el-time-picker is-range range-separator="至" start-placeholder="开始时间" end-placeholder="结束时间" placeholder="选择时间范围" v-model="form.date2" style="width: 50%;">
        </el-time-picker>
      </el-col>
    </el-form-item>
    <el-form-item>
      <el-col :span="10">
      <el-button type="primary" @click="onSubmit(reserve)">预定</el-button>
      <el-button>取消</el-button>
      </el-col>
    </el-form-item>
  </el-form>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MeetingReserve',
  data () {
    return {
      // value1: '',
      // value2: [new Date(2016, 9, 10, 8, 40), new Date(2016, 9, 10, 9, 40)]
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      base_url: 'http://localhost:8000/api/meeting/',
      rooms: 'null'
    }
  },
  methods: {
    getAll () {
      axios.get(this.base_url)
        .then(res => {
          this.rooms = res.data
        })
    },
    onSubmit (reserve) {

    }

  },
  mounted () {
    this.getAll()
  }
}
</script>
<style>
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
    align-items: center;
    align-content: center;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .el-form-item{
  text-align: center;
}
</style>
