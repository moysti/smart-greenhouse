<script>
  import Container from "./Container.vue";
  const socket = new WebSocket('ws://localhost:8080');

  export default {
    components: {
      Container
    },
    data() {
      return {
        level: null
      }
    },
    mounted() {
      socket.onmessage = (event) => {
        if (JSON.parse(event.data).type === 'tank') {
          const height = 10;
          let distance = JSON.parse(event.data).data;
          this.level = ((height - distance) / height) * 100;
        }
      };
    },
    methods: {

    }
  }

</script>

<template>
  <Container>
    <img class="tank-image" src="../assets/waterLevel.svg" alt="Tank"/>
    <div class="tank-number">
      {{ this.level + "%" }}
    </div>
  </Container>
</template>