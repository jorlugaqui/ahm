<template>
  <div>
    <alert :message=message :type=alertType v-if="showMessage"></alert>
    <form @submit.prevent="addMeasurement">
      <div class="form-group">
        <label for="sys">Sys</label>
        <input v-model="measurement.sys" type="number"
            class="form-control" id="sys" aria-describedby="syshelp">
        <small id="syshelp" class="form-text text-muted">
            Please enter your sys value
        </small>
      </div>
      <div class="form-group">
        <label for="dia">Dia</label>
        <input  v-model="measurement.dia" type="number"
            class="form-control" id="dia" aria-describedby="diahelp">
        <small id="diahelp" class="form-text text-muted">
            Please enter your dia value
        </small>
      </div>
      <div class="form-group">
        <label for="pul">Pul</label>
        <input  v-model="measurement.pul" type="number"
            class="form-control" id="pul" aria-describedby="pulhelp">
        <small id="pulhelp" class="form-text text-muted">
            Please enter your pul
        </small>
      </div>
      <div class="form-group">
        <label for="created">Created</label>
        <input v-model="measurement.created" type="date" class="form-control" id="created" readonly>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  name: 'Measurement',
  data() {
    return {
      measurement: {
        id: null,
        sys: 0,
        dia: 0,
        pul: 0,
        created: '',
      },
      showMessage: false,
      message: '',
      alertType: null,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    addMeasurement() {
      const { VUE_APP_API_HOST } = process.env;
      let httpMethod = null;
      let path = null;
      if (this.measurement.id === null) {
        httpMethod = 'post';
        path = `${VUE_APP_API_HOST}/v1/measurements`;
      } else {
        httpMethod = 'patch';
        path = `${VUE_APP_API_HOST}/v1/measurements/${this.measurement.id}`;
      }
      axios({
        url: path,
        method: httpMethod,
        data: this.measurement,
      })
        .then((res) => {
          this.measurement = res.data;
          this.showMessage = true;
          this.message = 'Measurement added';
          this.alertType = 'ok';
        })
        .catch((error) => {
          console.error(error);
          this.showMessage = true;
          this.message = error.response.data.message;
          this.alertType = 'error';
        });
    },
  },
};
</script>
