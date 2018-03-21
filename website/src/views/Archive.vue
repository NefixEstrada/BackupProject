<template>
  <div id="archive">
     <file-explorer :content="content"></file-explorer>
  </div>
</template>

<script>
import { myApi } from '../api.js'
import fileExplorer from '../components/FileExplorer.vue'

export default {
  name: 'archive',
  components: { fileExplorer },
  data () {
    return {
      content: {}
    }
  },
  created: function () {
    this.getArchive()
  },
  methods: {
    getArchive: function () {
      myApi.get(`backup/${this.$route.params.backupId}/${this.$route.params.archiveName}`).then((res) => {
        this.content = { 'path': '/', 'type': 'd', 'child': res.data.content }
      })
    }
  }

}
</script>
