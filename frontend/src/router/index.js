import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/components/Home.vue';
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';
import Dashboard from '@/components/Dashboard.vue';
import TrackerAdd from '@/components/TrackerAdd.vue';
import TrackerDel from '@/components/TrackerDel.vue';
import TrackerUpd from '@/components/TrackerUpd.vue';
import LogAdd from '@/components/LogAdd.vue';
import LogDel from '@/components/LogDel.vue';
import LogUpd from '@/components/LogUpd.vue';
import Tracker from '@/components/Tracker.vue';
import Error from '@/components/Error.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    //  component: () => import(/* webpackChunkName: "about" */ '../components/Home.vue'),
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      guest: true,
    },
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: {
      guest: true,
    },
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/:tracker_id',
    name: 'Tracker',
    component: Tracker,
  },
  {
    path: '//addtracker',
    name: 'Add Tracker',
    component: TrackerAdd,
  },
  {
    path: '/:tracker_id/delete',
    name: 'Delete Tracker',
    component: TrackerDel,
  },
  {
    path: '/:tracker_id/update',
    name: 'Update Tracker',
    component: TrackerUpd,
  },
  {
    path: '/:tracker_id/addlog',
    name: 'Add Log',
    component: LogAdd,
  },
  {
    path: '/:tracker_id/:log_id/deletelog',
    name: 'Delete Log',
    component: LogDel,
  },
  {
    path: '/:tracker_id/:log_id/updatelog',
    name: 'Update Log',
    component: LogUpd,
  },
  {
    path: '*',
    name: 'Error',
    component: Error,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: '/',
  routes,
});

export default router;
