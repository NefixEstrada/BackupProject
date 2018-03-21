<template>
  <div id="backups">
    <h1>Backups</h1>

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
          <div v-for="directory in props.row.directories" :key="directory">
            <b-badge>{{ directory }}</b-badge>
          </div>
        </td>
        <td>
          <b-row align-h="center">
            <b-button-group>
              <b-button variant="success" :to="'/backup/' + props.row.id">View</b-button>
              <b-button variant="danger" @click="deleteBackup(props.row.id)">Delete</b-button>
            </b-button-group>
          </b-row>
        </td>
      </template>
    </vue-good-table>

    <p v-else>No backups yet!</p>

    <b-button v-b-modal.newBackupModal variant="primary">Create Backup</b-button>
    <new-backup-modal></new-backup-modal>
  </div>
</template>

<script>
import { myApi } from '../api.js'
import ApiMessageAlert from '../components/ApiMessageAlert'
import { VueGoodTable } from 'vue-good-table'
import NewBackupModal from '../components/NewBackupModal'

export default {
  name: 'home',
  components: {
    ApiMessageAlert,
    VueGoodTable,
    NewBackupModal
  },
  data () {
    return {
      loading: true,
      columns: [
        {
          label: 'Name',
          field: 'name'
        },
        {
          label: 'Path',
          field: 'path'
        },
        {
          label: 'Directories'
        },
        {
          label: 'Actions'
        }
      ],
      rows: []
    }
  },
  created: function () {
    this.getBackups()
  },
  methods: {
    getBackups: function () {
      this.loading = true
      myApi.get('backups').then((res) => {
        this.rows = res.data
        this.loading = false
      })
    },
    deleteBackup: function (backupId) {
      myApi.delete(`backup/${backupId}`).then((res) => {
        this.getBackups()
        this.$refs.apiMessage.setContent(res)
      })
    }
  }
}
</script>

<style lang="sass">
#backups
  margin:
    top: 50px

  .data-table
    margin:
      top: 25px
      bottom: 25px
</style>
