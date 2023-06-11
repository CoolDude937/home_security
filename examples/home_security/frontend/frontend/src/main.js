import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import VueRouter from "vue-router";

Vue.config.productionTip = false;
Vue.prototype.$http = axios;
Vue.use(VueRouter);

new Vue({
    router,
    render: (h) => h(App),
}).$mount("#app");
