<template>
  <font-awesome-icon :icon="setIcon()"></font-awesome-icon>
</template>

<script>
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

export default {
  name: 'fileIcon',
  components: {
    FontAwesomeIcon
  },
  props: {
    content: Object
  },
  methods: {
    getFileExtension: function () {
      var fileName = this.content.path.split('/')
      fileName = fileName[fileName.length - 1]
      const extension = fileName.split('.')
      if (extension.length <= 1) {
        return null
      } else {
        return extension[extension.length - 1]
      }
    },
    setIcon: function () {
      const extension = this.getFileExtension()

      if (this.content.type === 'd') {
        return ['fas', 'folder']
      } else if (extension === 'png' || extension === 'jpg') {
        return ['far', 'file-image']
      } else {
        return ['far', 'file']
      }
    }
  }
}
</script>
