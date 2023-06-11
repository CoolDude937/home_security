<template>
    <div>
        <p align="center">
            <iframe
                :src="flaskAppUrl"
                style="width: 645px; height: 485px"
            ></iframe>
        </p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            flaskAppUrl: "http://127.0.0.1:5000//video_feed",
        };
    },
};
// import { checkVideoFormatsSupport } from "./videoSupport";
// export default {
//     mounted() {
//         // Call the function to check video format support
//         checkVideoFormatsSupport();
//         const videoElement = this.$refs.videoPlayer;

//         // Set the src attribute to the URL of the video stream endpoint
//         videoElement.src = "http://127.0.0.1:5000//video_feed";

//         // Load and play the video
//         videoElement.load();
//         videoElement.play();
//     },
// };
</script>

<!-- <style>
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
</style> -->
