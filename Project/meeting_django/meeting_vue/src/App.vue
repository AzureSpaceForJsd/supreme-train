<template>
  <div id="app">
    <el-container>
      <!--  header -->
      <el-header>
        <el-col :xs="24" :sm="24" :offset="6">
          <el-menu :default-active="$route.path" class="el-menu-vertical-demo" mode="horizontal" router>
            <el-menu-item class="hidden-sm-and-down"><img src="./assets/logo.png" style="width: 30px; height: 30px;"></el-menu-item>
            <el-menu-item index="/"><i class="el-icon-s-data"></i><span class="hidden-sm-and-down">预定状况</span></el-menu-item>
            <el-menu-item index="/user/login" v-if="!islogin" class="hidden-sm-and-down"><i class="el-icon-s-order"></i><span class="hidden-sm-and-down">Order</span></el-menu-item>
            <div v-else>
              <el-menu-item index="/Order/MeetingReserve" v-if="!islogin" class="hidden-sm-and-down"><i class="el-icon-edit"></i><span class="hidden-sm-and-down">Order</span></el-menu-item>
            </div>
            <el-submenu index="1">
              <template slot="title"><i class="el-icon-user"></i><span class="hidden-sm-and-down">UserHome</span></template>
              <div>
                <el-menu-item index="/user/login" v-if="!islogin">登录</el-menu-item>
                <div v-else>
                  <el-menu-item index="/user/root">{{ username }}</el-menu-item>
                  <el-menu-item @click="logout">Logout</el-menu-item>
                </div>

              </div>
            </el-submenu>
          </el-menu>
        </el-col>
      </el-header>

      <!--        导航栏-->
      <el-main :xs="24">

          <router-view></router-view>

      </el-main>
    </el-container>

  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      loading: true,
      num: null,
      islogin: false,
      username: ''
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    logout: function () {
      this.$axios.get('/apis/user/logout')
        .then(response => {
          // 重载界面
          window.location.reload()
        })
    }
  },
  created () {
    this.$axios.post('/apis/add?access=add_access&aa=32&kk=34', {access: 'access'})
      .then(response => {
        this.$axios.get('/apis/get_info?num=true&aa=66')
          .then(response => {
            this.loading = false
            this.num = response.data.num
          })
      }, () => {
        console.log('这里出错了.')
      })
    this.$axios.get('/apis/user/getstatus')
      .then(response => {
        if (response.data.status === 0) {
          this.islogin = true
          this.username = response.data.username
        }
      })
  }
}
</script>

<style>

</style>
