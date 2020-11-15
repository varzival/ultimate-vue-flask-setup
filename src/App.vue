<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png" />
        <nav>
            <router-link to="/">Home</router-link> |
            <router-link to="/api-test">Test Api</router-link> |
            <router-link to="/login-test">Test Login</router-link>
        </nav>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: "App"
};
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
