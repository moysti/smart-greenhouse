<script>
  import Container from "./Container.vue";

  export default {
    components: {
      Container
    },
    data() {
      return {
        tankLevel: 89,
        light: false,
        video: true,
      }
    },
    mounted() {

    },
    methods: {
      async controlLight() {
        this.light = !this.light;

        try {
          const res = await fetch('http://localhost:3000/publish', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              topic: 'greenhouse/light',
              message: this.light,
            }),
          });

          const data = await res.json();
          if (!data.success) {
            console.error('Failed to send message: ', data.error);
          }
        } catch (err) {
          console.error('Error sending request: ', err);
        }
      },
      toggleVideo() {
        this.video = !this.video;
        this.$emit('toggleVideo', this.video)
      },
      snapshot() {
        const now = new Date();
        const day = String(now.getDate()).padStart(2, '0');
        const month = String(now.getMonth() + 1).padStart(2, '0');
        const year = now.getFullYear();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        console.log(`Snapshot taken at ${day}.${month}.${year} ${hours}:${minutes}:${seconds}`
        );
      },
    },
    emits: [
      'toggleVideo'
    ]
  }
</script>

<template>
  <Container>
      <div class="button-container">
        <button :class="light ? 'light-active' : 'light-inactive'" @click="this.controlLight()">Toggle Light <i class="fa fa-lightbulb-o" aria-hidden="true"/></button>
        <button class="video-button" @click="this.toggleVideo()">{{ (video ? "Turn Off" : "Turn On") }} <i class="fa fa-video-camera" aria-hidden="true"/> </button>
        <!-- <button class="water-button" @click="this.snapshot()"> Snapshot </button> -->
      </div>
  </Container>
</template>