<template>
    <div id="app">
        <head>
            <link
                rel="stylesheet"
                href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                crossorigin="anonymous"
            />
            <title>Todos</title>
        </head>

        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="/"> Andy's Web App </a>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mx-auto">
                    <li>
                        <a class="nav-link" href="/"> Home </a>
                    </li>
                    <li>
                        <a class="nav-link" href="/face-recognition"
                            >Face Recognition</a
                        >
                    </li>
                    <li>
                        <a class="nav-link" href="/userlist">
                            Face Recognition User List
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
        <router-view> </router-view>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            image: null,
        };
    },

    methods: {
        uploadImage(event) {
            this.image = event.target.files[0];
        },
        recognize() {
            const formData = new FormData();
            formData.append("image", this.image);

            axios
                .post("http://127.0.0.1:5000//video_feed", formData)
                .then((response) => {
                    console.log(response.data.result);
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
};
</script>

<style>
#app {
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
nav {
    padding: 30px;
}

nav a {
    font-weight: bold;
    color: #2c3e50;
}

nav a.router-link-exact-active {
    color: #42b983;
}
</style>
