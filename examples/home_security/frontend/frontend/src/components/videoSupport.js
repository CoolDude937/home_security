// videoSupport.js

export function checkVideoFormatsSupport() {
    const videoElement = document.createElement("video");

    // Check if the browser supports the MP4 video format
    const mp4Support = videoElement.canPlayType("video/mp4");
    console.log("MP4 support:", mp4Support);

    // Check if the browser supports the WebM video format
    const webmSupport = videoElement.canPlayType("video/webm");
    console.log("WebM support:", webmSupport);

    // Check if the browser supports the Ogg video format
    const oggSupport = videoElement.canPlayType("video/ogg");
    console.log("Ogg support:", oggSupport);
}
