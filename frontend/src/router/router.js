import Vue from 'vue';
import Router from 'vue-router';
import vHome from '../components/v-home';
import vAuth from '../components/otherPages/v-authentication';
import vProfile from '../components/otherPages/v-profile';
import store from '../vuex/store';
import vLogin from '../components/otherPages/v-login';
Vue.use(Router);
let routes = [{
        name: "home",
        path: "/",
        component: vHome
    },
    {
        name: "login",
        path: "/login",
        component: vLogin
    },
    {
        name: "profile",
        path: "/profile",
        component: vProfile,
        beforeEnter(to, from, next){
            if(store.state.idToken)next();
            else next('./registration');
        }
    },
    {
        name: "documentation",
        path: "/docs"
    },
    {
        name: "about",
        path: "/about"
    },
    {
        name: "contacts",
        path: "/contacts"
    },
    {
        name: "registration",
        path: "/registration",
        component: vAuth,
    },
    {
        name: "catchAll",
        component: vHome,
        path: "*"
    }
];
let router = new Router({
    routes: routes,
    mode: 'history'
});
export default router;