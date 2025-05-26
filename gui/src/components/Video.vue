<script>
  import Container from "./Container.vue";

  export default {
    components: {
      Container
    },
    props: {
      video: Boolean
    },
    data() {
      return {
      }
    },
    mounted() {
      this.getWebcam();
    },
    methods: {
      getWebcam() {
        const video = document.querySelector("#stream");

        if (navigator.mediaDevices.getUserMedia) {
          navigator.mediaDevices.getUserMedia({ video: true })
              .then(function (stream) {
                video.srcObject = stream;
              })
              .catch(function (error) {
                console.log("Something went wrong getting webcam stream: " + error);
              });
        }
      }
    },
    watch: {
      video(newVal) {
        if (!newVal) {
          console.log('DISABLE STREAM');
        } else {
          console.log('ENABLE STREAM');
        }
      }
    }
  }
</script>

<template>
  <Container>
    <video autoplay id="stream" class="stream" controls poster="https://i.kym-cdn.com/photos/images/newsfeed/002/931/608/72e" width="300"></video>
  </Container>
</template>