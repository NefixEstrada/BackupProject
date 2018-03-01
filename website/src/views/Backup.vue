<template>
  <!-- TODO: Use bootstrap, make things prettier, use VueGoodTables... -->
  <div>
    <ul v-if="backup.archives.lenght !== 0">
      <li v-for="archive in backup.archives" :key="archive.id">{{ archive.name }}</li>
    </ul>
    <p v-else>No archives yet!</p>
    <p>{{ backup.archives.lenght }}</p>
    <p v-if="loading === true">Loading...</p>
    <button @click="createArchive">Create Archive!</button>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import { myApi } from '../api.js'

export default {
  data () {
    return {
      backup: {
        archives: []
      },
      message: '',
      loading: true
    }
  },
  created: function () {
    this.getBackup()
  },
  methods: {
    getBackup: function () {
      myApi.get(`backup/${this.$route.params.backupId}`).then((res) => {
        this.backup = res.data
        this.loading = false
      })
    },
    createArchive: function () {
      myApi.post(`backup/${this.$route.params.backupId}`).then((res) => {
        this.message = res.data
      })
    }
  }
}
</script>
