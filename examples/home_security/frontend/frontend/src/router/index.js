import Vue from "vue";
import Router from "vue-router";
import HomeView from "../views/HomeView.vue";
import FaceRecognition from "../components/FaceRecognition.vue";
import UserList from "../components/UserList.vue";

Vue.use(Router);

const routes = [
    {
        path: "/",
        name: "home",
        component: HomeView,
    },
    {
        path: "/face-recognition",
        name: "FaceRecognition",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: FaceRecognition,
    },
    {
        path: "/userlist",
        name: "UserList",
        component: UserList,
    },
];

const router = new Router({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;
