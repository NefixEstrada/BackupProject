<template>
  <!-- TODO: Use bootstrap, make things prettier, use VueGoodTables... -->
  <div id="backup">
    <h1>{{ backupName }}</h1>

    <api-message-alert ref="apiMessage"></api-message-alert>
    <p v-if="loading === true">Loading...</p>

    <vue-good-table
      v-else-if="rows.length !== 0"
      :globalSearch="true"
      :columns="columns"
      :rows="rows"
      class="data-table">

      <template slot="table-row-after" slot-scope="props">
        <td>
          <b-row align-h="center">
            <b-button-group>
              <b-button variant="success" :to="$route.fullPath + '/' + props.row.name">View</b-button>
              <b-button variant="info">Edit</b-button>
              <b-button variant="danger" @click="deleteArchive(props.row.name)">Delete</b-button>
            </b-button-group>
          </b-row>
        </td>
      </template>

    </vue-good-table>

    <p v-else>No archives yet!</p>

    <b-button variant="primary" @click="createArchive">Create archive</b-button>
  </div>
</template>

<script>
import { myApi } from '../api.js'
import ApiMessageAlert from '../components/ApiMessageAlert'
import { VueGoodTable } from 'vue-good-table'

export default {
  name: 'backup',
  components: {
    ApiMessageAlert,
    VueGoodTable
  },
  data () {
    return {
      loading: true,
      backupName: '',
      columns: [
        {
          label: 'Name',
          field: 'name'
        },
        {
          label: 'Time',
          field: 'time'
        },
        {
          label: 'Actions'
        }
      ],
      rows: []
    }
  },
  created: function () {
    this.getBackup()
  },
  methods: {
    getBackup: function () {
      myApi.get(`backup/${this.$route.params.backupId}`).then((res) => {
        this.rows = res.data.archives
        this.loading = false
      })
    },
    createArchive: function () {
      myApi.post(`backup/${this.$route.params.backupId}`).then((res) => {
        this.getBackup()
        this.$refs.apiMessage.setContent(res)
      })
    },
    deleteArchive: function (archiveName) {
      myApi.delete(`backup/${this.$route.params.backupId}/${archiveName}`).then((res) => {
        this.getBackup()
        this.$refs.apiMessage.setContent(res)
      })
    }
  }
}
</script>

<style lang="sass">
#backup
  margin:
    top: 50px

  .data-table
    margin:
      top: 25px
      bottom: 25px
</style>
