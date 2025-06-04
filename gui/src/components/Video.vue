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

    },
    methods: {

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
    <img src="@/assets/received.jpg" alt="Video Stream" class="stream" v-if="video"/>
    <img src="@/assets/pervasive.png" alt="Video Disabled" class="stream" v-else="video"/>
  </Container>
</template>