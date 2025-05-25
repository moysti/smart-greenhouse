<script>
import DateTime from "@/components/DateTime.vue";
import Temperature from "@/components/Temperature.vue";
import Humidity from "@/components/Humidity.vue";
import Terminal from "@/components/Terminal.vue";
import Stats from "@/components/Stats.vue";
import Video from "@/components/Video.vue";
import Tank from "@/components/Tank.vue";

export default {
  components: {
    DateTime, Temperature, Humidity, Terminal, Stats, Video, Tank
  },
  data() {
    return {

    }
  },
  mounted() {

  },
  methods: {

  }
}
</script>

<template>
  <DateTime/>
  <div class="container-wrapper">
    <Temperature/>
    <Humidity/>
    <Stats/>
    <Tank/>
    <Video/>
    <Terminal/>
  </div>

</template>

<style src="../src/css/main.css"/>
