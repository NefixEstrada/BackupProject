<template>
  <div class="file-explorer">
    <path-explorer :path="contentToShow.path"></path-explorer>
    <file-tree :content="contentToShow.child"></file-tree>
  </div>
</template>

<script>
import fileTree from './FileTree'
import pathExplorer from './PathExplorer'

export default {
  name: 'fileExplorer',
  components: {
    fileTree,
    pathExplorer
  },
  props: {
    content: Object
  },
  data () {
    return {
      contentToShow: {
        path: 'Loading...',
        child: []
      },
      breadcrumbContent: ['Loading...']
    }
  },
  watch: {
    content: function () {
      this.contentToShow = this.content
    }
  },
  methods: {
    changeFolder: function (folderPath) {
      this.contentToShow = this.getChild(folderPath, this.content)
    },
    getChild: function (folderPath, currentFolder) {
      if (currentFolder.path === folderPath) {
        return currentFolder
      }
      if (currentFolder.type === 'd' && currentFolder.path) {
        for (let currentChild of currentFolder.child) {
          if (currentChild.path === folderPath) {
            return currentChild
          }
          let result = this.getChild(folderPath, currentChild)
          if (result !== false) {
            return result
          }
        }
      }
      return false
    }
  }
}
</script>

<style lang="sass">
.file
  list:
    style: none
</style>
