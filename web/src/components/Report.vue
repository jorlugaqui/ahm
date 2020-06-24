<template>
  <div>
    <h3>Report </h3>
    <div class="input-group">
      <input v-model="period" placeholder="Type a period">
      <button type="button" class="btn btn-primary" v-on:click="getReport"> Search </button>
    </div>
    <br>
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
    <alert :message=errorMessage :type="'error'" v-if="showMessage"></alert>
  </div>
</template>

<script>
import fetchReport from '@/api.js';
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
      fetchReport(this.period)
        .then((res) => {
          this.report = res.data;
          this.showMessage = false;
          this.errorMessage = '';
        })
        .catch((error) => {
          console.error(error);
          this.report = {};
          this.showMessage = true;
          this.errorMessage = error.response.data.message;
        });
    },
  },
};
</script>
