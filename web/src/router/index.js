import Vue from 'vue';
import VueRouter from 'vue-router';
import Report from '../components/Report.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Report',
    component: Report,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
