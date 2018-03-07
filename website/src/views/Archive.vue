<template>
  <div id="archive">
    <p v-for="item in content" :key="item">{{ item.path }}</p>
  </div>
</template>

<script>
import { myApi } from '../api.js'

export default {
  name: 'archive',
  data () {
    return {
      content: []
    }
  },
  created: function () {
    this.getArchive()
  },
  methods: {
    getArchive: function () {
      myApi.get(`backup/${this.$route.params.backupId}/${this.$route.params.archiveName}`).then((res) => {        
        this.content = res.data.content
      })
    }
  }

}
</script>
