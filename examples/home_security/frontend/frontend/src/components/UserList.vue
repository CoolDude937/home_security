<template>
    <div>
        <ul>
            <li v-for="user in users" :key="user.id">
                {{ user.name }} - {{ user.face_encoding }}
            </li>
        </ul>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            users: [],
        };
    },
    mounted() {
        this.fetchUsers();
    },
    methods: {
        fetchUsers() {
            axios
                .get("http://127.0.0.1:5000//userlist")
                .then((response) => {
                    this.users = response.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
};
</script>
