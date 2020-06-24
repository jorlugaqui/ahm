<template>
  <div>
    <h3>Report </h3>
    <div class="input-group">
      <input v-model="period" placeholder="Type a period">
      <button type="button" class="btn btn-primary" v-on:click="getReport"> Search </button>
    </div>
    <br>
    <div class="table-responsive">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Date</th>
          <th scope="col">Sys</th>
          <th scope="col">Dia</th>
          <th scope="col">Pul</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="measurement in report.values" :key="measurement.date"
          v-bind:class="{'table-danger': !measurement.ok}">
          <th scope="row" >{{ measurement.date }}</th>
          <td>{{ measurement.sys }}</td>
          <td>{{ measurement.dia }}</td>
          <td>{{ measurement.pul }}</td>
        </tr>
      </tbody>
    </table>
    </div>
    <alert :message=errorMessage :type="'error'" v-if="showMessage"></alert>
  </div>
</template>

<script>
import api from '@/api.js';
import Alert from './Alert.vue';

export default {
  name: 'Report',
  data() {
    return {
      report: '',
      period: '',
      showMessage: false,
      errorMessage: '',
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getReport() {
      api.fetchReport(this.period)
        .then(api.parseJSON)
        .then((response) => {
          if (response.ok) {
            return Promise.resolve(response.json);
          }
          return Promise.reject(response.json);
        })
        .then((data) => {
          this.report = data;
          this.showMessage = false;
          this.errorMessage = '';
        })
        .catch((error) => {
          this.report = {};
          this.showMessage = true;
          this.errorMessage = error.message;
        });
    },
  },
};
</script>
