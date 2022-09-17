import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Dashboard from '@/components/Dashboard'
import Tracker from '@/components/Tracker'
import Tracker_Add from '@/components/Tracker_Add'
import Tracker_Del from '@/components/Tracker_Del'
import Tracker_Upd from '@/components/Tracker_Upd'
import Log_Add from '@/components/Log_Add'
import Log_Del from '@/components/Log_Del'
import Log_Upd from '@/components/Log_Upd'



Vue.use(Router);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            guest: true
        }
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: { 
            guest: true
        }
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
        meta: { 
            guest: true
        }
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
        path: '/addtracker',
        name: 'Add Tracker',
        component: Tracker_Add,
    },
    {
        path: '/:tracker_id/delete',
        name: 'Delete Tracker',
        component: Tracker_Del,
    },
    {
        path: '/:tracker_id/update',
        name: 'Update Tracker',
        component: Tracker_Upd,
    },
    {
        path: '/:tracker_id/addlog',
        name: 'Add Log',
        component: Log_Add,
    },
    {
        path: '/:tracker_id/:log_id/deletelog',
        name: 'Delete Log',
        component: Log_Del,
    },
    {
        path: '/:tracker_id/:log_id/updatelog',
        name: 'Update Log',
        component: Log_Upd,
    },
];



const router = new Router({
  mode: 'history',
  routes,
  base: '/'
});

// router.beforeEach((to, from, next) => {
//   if(to.matched.some(record => record.meta.requiresAuth)) {
//       if (localStorage.getItem('usertoken') == null) {
//         next({
//             path: '/login',
//             params: { nextUrl: to.fullPath }
//         })
//       }
//       else{
//         next()
//       }
//   } else if(to.matched.some(record => record.meta.guest)) {
//       if(localStorage.getItem('usertoken') == null){
//           next()
//       }
//       else{
//           next()
//       }
//   }else {
//       next() 
//   }
//})

export default router;