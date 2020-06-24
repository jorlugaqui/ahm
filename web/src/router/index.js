import Vue from 'vue';
import VueRouter from 'vue-router';
import Report from '../components/Report.vue';
import Measurement from '../components/Measurement.vue';
import MeasurementUpdate from '../components/MeasurementUpdate.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'measurement',
    component: Measurement,
  },
  {
    path: '/update/:id',
    name: 'updateMeasurement',
    component: MeasurementUpdate,
  },
  {
    path: '/report',
    name: 'report',
    component: Report,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
