<template>
  <div>
    <!-- TODO: clearAlert() doesn't get called -->
    <b-alert :variant="status" dismissible :show="showAlert" @dismissed="clearAlert()">{{ message }}</b-alert>
  </div>
</template>

<script>
export default {
  name: 'ApiMessageAlert',
  data () {
    return {
      message: '',
      status: '',
      showAlert: false
    }
  },
  methods: {
    setContent: function (res) {
      var statusCode = res.status
      this.message = res.data.message
      if ((statusCode === 200) || (statusCode === 201)) {
        this.status = 'success'
      } else {
        this.status = 'danger'
      }
      this.showAlert = true
    },
    clearAlert: function () {
      this.message = ''
      this.status = ''
      this.showAlert = false
    }
  }
}
</script>
