<template>
  <div id="MeetingReserve" v-loading="false" style="margin: 0 auto">
    <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12" :span="6" :offset="6">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="会议室 " label-width="80px" label-position="center">
        <el-select v-model="form.name" placeholder="请选择会议室">
          <el-option
            v-for="room in rooms"
            :key="room.roomNo"
            :label="room.roomName"
            :value="room.roomName">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="预定日期">
        <el-date-picker type="date" placeholder="选择日期" v-model="form.date" style="width: 80%;" value-format="timestamp"></el-date-picker>
      </el-form-item>
    <el-form-item label="预定时间">
        <el-time-select
          placeholder="起始时间"
          v-model="form.startTime"
          :picker-options="{
            start: '08:30',
            step: '00:15',
            end: '18:30'
          }">
        </el-time-select>
        <el-time-select
          placeholder="结束时间"
          v-model="form.endTime"
          :picker-options="{
          start: '08:30',
          step: '00:15',
          end: '18:30',
          minTime: form.startTime
          }">
        </el-time-select>
    </el-form-item>
    <el-form-item>
      <el-col :span="10" :offset="6">
      <el-button type="primary" @click="order('data')">预定</el-button>
      <el-button>取消</el-button>
      </el-col>
    </el-form-item>
  </el-form>
  </el-col>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MeetingReserve',
  data () {
    return {
      form: {
        name: '',
        date: '',
        startTime: '',
        endTime: ''
      },
      base_url: 'apis/meetingrooms',
      post_url: 'apis/orderMeetingroom',
      resFlag: '',
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
    order: function (Dataset) {
      this.$refs[Dataset].validata((valid) => {
        if (valid) {
          this.$axios.post(this.post_url, {
            name: this.data.name,
            date: this.data.date,
            strTime: this.data.startTime,
            endTime: this.data.endTime
          })
            .then(Response => {
              if (Response.data.orderFlag === 0) {
                this.$message({
                  message: '预定成功',
                  type: 'success'
                })
              } else {
                this.$message.error('预约失败，当前时间段已有预约')
              }
            })
        } else {
          return false
        }
      })
    }
  },
  mounted () {
    this.getAll()
  }
}
</script>
<style>
  .el-row {
    margin-bottom: 10px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
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
