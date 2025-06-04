<script>
  import Container from "./Container.vue";
  const socket = new WebSocket('ws://localhost:8080');

  export default {
    components: {
      Container
    },
    data() {
      return {
        temp: null,
      }
    },
    mounted() {
      socket.onmessage = (event) => {
        if (JSON.parse(event.data).type === 'temperature') {
          this.temp = JSON.parse(event.data).data;
        }
      };
    },
    methods: {

    }
}
</script>

<template>
  <Container>
    <img class="temperature-image" src="../assets/thermometer.svg" alt="Temperature"/>
    <div class="temperature-number">
      {{ this.temp + "°C" }}
    </div>
  </Container>
</template>