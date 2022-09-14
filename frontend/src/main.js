// import { createApp } from 'vue'
import Vue from 'vue'
import App from './App.vue'
import router from './router/router'

Vue.config.productionTip = false

// const app = createApp(App);
// app.use(router);
// app.mount('#app');

var app = new Vue({
  el: '#app',
  router: router,
  data: {},
  methods: {},
  render: h => h(App)
})

