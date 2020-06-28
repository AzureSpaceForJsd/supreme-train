import axios from '..assets/js/axios'


meetingRoom: {
    roomNo: '';
    roomName: '';
    roomAddr: '';
    roomSts: '';
    roomLevel: '';
    roomMedia: ''
};//会议室详情

getMeetingRoom(){
    axios.Get({
        url: 'api/meetingrooms',
        params: {
        },
        callback: (res) => {
            let data = res.data
            state.meetingRoom = {
                roomNo: data['roomNo'],
                roomName: data['roomName'],
                roomAddr: data['roomAddr'],
                roomSts: data['roomSts'],
                roomLevel: data['roomLevel'],
                roomMedia: data['roomMedia']
            }
            state.loading = false
        }
    })
    return data
}