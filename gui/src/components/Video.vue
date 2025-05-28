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
    <img src="@/assets/received.jpg" alt="Video Stream" class="stream"/>
  </Container>
</template>