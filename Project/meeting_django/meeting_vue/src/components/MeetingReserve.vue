<template>
<div>
  <div style="width:100%;text-align:center">
    <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="会议室 " label-width="80px" label-position="center">
      <el-col :span="10">
        <el-select v-model="form.value" placeholder="请选择会议室">
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
        <el-date-picker type="date" placeholder="选择日期" v-model="form.date" style="width: 50%;" value-format="timestamp"></el-date-picker>
      </el-col>
    </el-form-item>
    <el-form-item label="预定时间">
      <el-col :span="11">
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
import {mapState, mapActions} from 'vuex'

export default {
  name: 'MeetingReserve',
  data () {
    return {
      form: {
        value: '',
        date: '',
        startTime: '',
        endTime: ''
      },
      base_url: 'http://localhost:8000/api/meeting/',
      post_url: '',
      resFlag: '',
      rooms: 'null'
    }
  },
  computed: {
    ...mapState({
      rooms: state => state.ArchiveStore.meetingRoom
    })
  },
  methods: {
    ...mapActions([
      'getMeetingRoom'
    ]),
    getAll () {
      axios.get(this.base_url)
        .then(res => {
          this.rooms = res.data
        })
    },
    reserveRoom () {
      axios.post(this.post_url, this.form)
        .then(res => {
          this.resFlag = res.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    onSubmit: function () {

    },
    getMeetingRoom () {
      this.getMeetingRoom()
    }
  },
  activated: function () {
    this.rooms = getMeetingRoom()
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
