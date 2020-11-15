import HelloWorld from "../components/HelloWorld";
import ApiTest from "../components/ApiTest";
import LoginTest from "../components/LoginTest";

export default [
    { path: "/", component: HelloWorld },
    { path: "/api-test", component: ApiTest },
    { path: "/login-test", component: LoginTest }
];
