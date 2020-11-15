import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);

import App from "./App.vue";
import routes from "./utils/routes";

Vue.config.productionTip = false;

const router = new VueRouter({
    base: __dirname,
    routes: routes
});

new Vue({
    render: h => h(App),
    router
}).$mount("#app");
