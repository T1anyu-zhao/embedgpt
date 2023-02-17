import { createWebHistory, createRouter } from "vue-router";
import Home from "@/pages/Home.vue";
import User from "@/pages/User.vue";
import Login from "@/pages/Login.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/User",
    name: "User",
    component: User,
  },
  {
    path: "/Login",
    name: "Login",
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;