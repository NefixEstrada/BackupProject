<template>
  <div class="path-explorer">
    <ol class="breadcrumb">
      <li class="breadcrumb-item" v-if="path !== '/'">
        <a :href="'/#' + $route.fullPath" @click="goToRoot()"><font-awesome-icon :icon="['fas', 'hashtag']"></font-awesome-icon></a>
      </li>
      <li v-for="(directory, index) in path.split('/')" :key="index" class="breadcrumb-item">
        <a v-if="index !== path.split('/').length - 1" :href="'/#' + $route.fullPath" @click="changeFolderUsingPathExplorer($event, path)" :index="index">{{ directory }}</a>
        <span v-else>{{ directory }}</span>
      </li>
    </ol>
  </div>
</template>

<script>
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

export default {
  name: 'pathExplorer',
  components: { FontAwesomeIcon },
  props: {
    path: String
  },
  methods: {
    changeFolderUsingPathExplorer: function (event, currentFolderPath) {
      const index = event.target.attributes.index.value
      const parentFolderPath = currentFolderPath.split('/').slice(0, Number(index) + Number(1)).join('/')

      this.$parent.changeFolder(parentFolderPath)
    },
    goToRoot: function () {
      this.$parent.changeFolder('/')
    }
  }
}
</script>
