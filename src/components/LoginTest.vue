<template>
    <div id="content">
        <div v-if="!logged_in">
            Username:
            <input type="text" v-model="login_name" />
            <button @click="login">Login</button>
        </div>
        <div v-else>
            Logged in as: {{ myname }}
            <div>
                <button @click="logout">Logout</button>
            </div>
        </div>
        <div v-html="error_msg"></div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "ApiTest",
    data() {
        return {
            error_msg: "",
            login_name: "",
            myname: ""
        };
    },
    computed: {
        logged_in() {
            return this.myname != "";
        }
    },
    mounted() {
        this.checkMyName();
    },
    methods: {
        login() {
            axios
                .get("/api/login", {
                    params: { username: this.login_name },
                    withCredentials: true
                })
                .then(this.checkMyName())
                .catch(
                    error =>
                        (this.error_msg = error.response
                            ? error.response.data
                            : "")
                );
        },
        logout() {
            axios
                .get("/api/logout")
                .then(this.checkMyName())
                .catch(
                    error =>
                        (this.error_msg = error.response
                            ? error.response.data
                            : "")
                );
        },
        checkMyName() {
            // Timeout needed, otherwise cookie will not be updated after first request
            const vm = this;
            setTimeout(function() {
                axios
                    .get("/api/myname")
                    .then(
                        response =>
                            (vm.myname = response.data.username
                                ? response.data.username
                                : "")
                    )
                    .catch(
                        error =>
                            (vm.error_msg = error.response
                                ? error.response.data
                                : "")
                    );
            }, 100);
        }
    }
};
</script>

<style scoped>
#content {
    margin: 10px;
}
</style>
