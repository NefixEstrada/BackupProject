<template>
  <div>
    <b-modal id="newBackupModal" ref="newBackupModal" title="Create a new Backup" disable-ok>
      <b-form @submit="createBackup" id="newBackupForm">
        <b-form-group id="name-input-group" label="Name:" label-for="name-input">
          <b-form-input id="name-input" type="text" placeholder="Name" v-model="newBackupName"></b-form-input>
        </b-form-group>

        <b-form-group id="directories-input-group" label="Directories (separated by commas and spaces):" label-for="directories-input">
          <b-form-input id="directories-input" type="text" placeholder="Directories" v-model="newBackupDirectories"></b-form-input>
        </b-form-group>
      </b-form>
      <b-container slot="modal-footer">
        <b-row align-h="end">
          <b-button type="submit" variant="primary" slot="modal-ok" form="newBackupForm">Create Backup!</b-button>
        </b-row>
      </b-container>
    </b-modal>

  </div>
</template>

<script>
import { myApi } from '../api.js'

export default {
  name: 'newBackup',
  data () {
    return {
      newBackupName: '',
      newBackupDirectories: ''
    }
  },
  methods: {
    createBackup: function () {
      myApi.post('backups', {
        name: this.newBackupName,
        directories: this.newBackupDirectories
      }).then((res) => {
        this.$refs.newBackupModal.hide()
        this.cleanForm()
        this.$parent.getBackups()
      })
    },
    cleanForm: function () {
      this.newBackupName = ''
      this.newBackupDirectories = ''
    }
  }
}
</script>
