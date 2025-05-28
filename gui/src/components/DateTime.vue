<script>
  export default {
    components: {

    },
    data() {
      return {
        date: '',
        time: new Date().getTime(),
      }
    },
    mounted() {
      this.updateDateTime();
      this.timer = setInterval(this.updateDateTime, 1000);
    },
    methods: {
      updateDateTime() {
        const now = new Date();
        const day = String(now.getDate()).padStart(2, '0');
        const month = String(now.getMonth() + 1).padStart(2, '0');
        const year = now.getFullYear();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');

        this.date = `${day}.${month}.${year}`;
        this.time = ` ${hours}:${minutes}:${seconds}`;
      }
    },
    beforeDestroy() {
      clearInterval(this.timer);
    }
  }
</script>

<template>
  <div class="date-time">
    <div class="time">
      {{ this.time }}
    </div>
    <div class="date">
      {{ this.date }}
    </div>
  </div>
</template>