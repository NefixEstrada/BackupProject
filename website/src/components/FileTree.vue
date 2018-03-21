<template>
  <div class="tree">
    <vue-good-table
      :globalSearch="true"
      :columns="columns"
      :rows="content"
      class="data-table">

      <template slot="table-row-before" slot-scope="props">
        <td>
          <b-row align-h="center" align-v="center">
            <b-button class="icon-button" disabled><b-row align-h="center" align-v="center"><file-icon :content="props.row"></file-icon></b-row></b-button>
          </b-row>
        </td>
      </template>

      <template slot="table-row-after" slot-scope="props">
        <td>
          <b-row align-h="center" align-v="center">
            <a :href="'/#' + $route.fullPath" v-if="props.row.type === 'd'" @click="$parent.changeFolder(props.row.path)">
              {{ props.row.name }}
            </a>
            <p v-else>{{ props.row.name }}</p>
          </b-row>
        </td>
        <td>
          <b-row align-h="center" align-v="center">
            <b-button variant="primary" class="icon-button"><b-row align-h="center" align-v="center"><font-awesome-icon :icon="['fas', 'cloud-download-alt']"></font-awesome-icon></b-row></b-button>
          </b-row>
        </td>
      </template>
    </vue-good-table>
  </div>
</template>

<script>
import FileIcon from './FileIcon'
import { VueGoodTable } from 'vue-good-table'
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

export default {
  name: 'fileTree',
  components: {
    FileIcon,
    VueGoodTable,
    FontAwesomeIcon
  },
  props: {
    content: Array
  },
  data () {
    return {
      isActive: false,
      columns: [
        {
          label: 'Type'
        },
        {
          label: 'Name'
        },
        {
          label: 'Download'
        }
      ]
    }
  },
  methods: {
    showChild: function (event) {
      this.isActive = !this.isActive
    }
  }
}
</script>

<style lang="sass">
.icon-button
  width: 40px
  height: 40px
</style>
