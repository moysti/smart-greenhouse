<script>
  import Container from "./Container.vue";

  export default {
    components: {
      Container

    },
    data() {
      return {
        tankLevel: 89,
        light: true,
        video: true
      }
    },
    mounted() {

    },
    methods: {
      toggleLight() {
        // do other shit
        this.light = !this.light;
      },
      toggleVideo() {
        this.video = !this.video;
      },
      water() {
        console.log("splish splash")
      }
    }
  }
</script>

<template>
  <Container>
      <div class="button-container">
        <button class="light" @click="this.toggleLight()">{{ (light ? "Turn Off"  : "Turn On") }} <i class="fa fa-lightbulb-o" aria-hidden="true"/></button>
        <button class="video-button" @click="this.toggleVideo()">{{ (video ? "Turn Off" : "Turn On") }} <i class="fa fa-video-camera" aria-hidden="true"/> </button>
        <button class="water-button" @click="this.water()"> Water <i class="fa fa-tint" aria-hidden="true"/> </button>
      </div>
  </Container>
  <!--
  <div class="terminal">
  </div>
  -->
</template>