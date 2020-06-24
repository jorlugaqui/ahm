<template>
  <div class="table-responsive">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Sys</th>
          <th scope="col">Dia</th>
          <th scope="col">Pul</th>
          <th scope="col">Date</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ measurement.sys }}</td>
          <td>{{ measurement.dia }}</td>
          <td>{{ measurement.pul }}</td>
          <td>{{ measurement.created }}</td>
          <td>
            <router-link class="badge badge-primary"
              :to="{ name: 'updateMeasurement', params: { id: measurement.id }}">Edit
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'MeasurementDetail',
  props: ['measurement'],

};
</script>
