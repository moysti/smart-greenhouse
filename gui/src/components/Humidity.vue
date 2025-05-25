<script>
  import Container from "./Container.vue";
  const socket = new WebSocket('ws://localhost:8080');

  export default {
    components: {
      Container
    },
    data() {
      return {
        moisture: 63,
      }
    },
    mounted() {
      socket.onmessage = (event) => {
        if (JSON.parse(event.data).type === 'humidity') {
          this.moisture = JSON.parse(event.data).data;
        }
      };
    },
    methods: {

    }
  }
</script>

<template>
  <Container>
    <div class="moisture-number">
      {{ this.moisture + "%"}}
    </div>
    <img class="moisture-image" src="../assets/humidity.png" alt="Moisture">
  </Container>
</template>