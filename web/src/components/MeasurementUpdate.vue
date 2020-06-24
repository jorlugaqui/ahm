<template>
  <div>
    <alert :message=message :type=alertType v-if="showMessage"></alert>
    <form @submit.prevent="updateMeasurement">
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
      <button type="submit" class="btn btn-primary">Update</button>
    </form>
    <br>
  </div>
</template>

<script>
import api from '@/api.js';
import Alert from './Alert.vue';

export default {
  name: 'MeasurementUpdate',
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
    getMeasurement(id) {
      api.getMeasurement(id)
        .then(api.parseJSON)
        .then((response) => {
          if (response.ok) {
            return Promise.resolve(response.json);
          }
          return Promise.reject(response.json);
        })
        .then((data) => {
          this.measurement = data;
          this.showMessage = false;
        })
        .catch((error) => {
          this.showMessage = true;
          this.message = error.message;
          this.alertType = 'error';
        });
    },
    updateMeasurement() {
      api.updateMeasurement(this.measurement)
        .then(api.parseJSON)
        .then((response) => {
          if (response.ok) {
            return Promise.resolve(response.json);
          }
          return Promise.reject(response.json);
        })
        .then((data) => {
          this.measurement = data;
          this.showMessage = true;
          this.message = 'Measurement updated';
          this.alertType = 'ok';
          this.saveMeasurementOnLocal();
        })
        .catch((error) => {
          this.showMessage = true;
          this.message = error.message;
          this.alertType = 'error';
        });
    },
    saveMeasurementOnLocal() {
      localStorage.setItem('measurement', JSON.stringify(this.measurement));
    },
  },
  created() {
    const { id } = this.$route.params;
    if (!id) {
      this.showMessage = true;
      this.message = 'A measurement ID is required';
      this.alertType = 'error';
    }
    this.getMeasurement(id);
  },
};
</script>
