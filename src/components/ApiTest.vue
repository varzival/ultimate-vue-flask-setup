<template>
    <div id="content">
        <div class="loading" v-if="greetings === '' && error_msg === ''">
            Loading...
        </div>
        <div v-html="error_msg"></div>
        <div>
            {{ greetings }}
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "ApiTest",
    data() {
        return {
            greetings: "",
            error_msg: ""
        };
    },
    mounted() {
        axios
            .get("/api/greetings")
            .then(response => (this.greetings = response.data.text))
            .catch(
                error =>
                    (this.error_msg = error.response ? error.response.data : "")
            );
    }
};
</script>

<style scoped>
#content {
    margin: 10px;
}

.loading {
    margin: 10px;
}
</style>
