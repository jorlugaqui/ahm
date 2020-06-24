import Vue from 'vue';
import VueRouter from 'vue-router';
import Report from '../components/Report.vue';
import Measurement from '../components/Measurement.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'measurement',
    component: Measurement,
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
