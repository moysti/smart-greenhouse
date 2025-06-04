<script>
import Container from "./Container.vue";
import DateTime from "@/components/DateTime.vue";

export default {
  components: {
    DateTime,
    Container
  },
  data() {
    return {

    }
  },
  mounted() {

  },
  methods: {
    openStats() {
      document.getElementById('stats-dialog').showModal();
    },
    closeStats() {
      document.getElementById('stats-dialog').close();
    }
  }
}
</script>

<template>
  <Container>
    <!-- <img class="stats-image" src="../assets/stats-image.png" alt="Statistics" @click="openStats()"> -->
    <img src="@/assets/pervasive.png" alt="placeholder" class="stats-image">

    <!--
    <dialog id="stats-dialog" class="stats-dialog">
      <span class="close" @click="closeStats">x</span>
      <DateTime/>
      <div class="stats">
        <div class="snapshot">
          <div class="stats-header">SNAPSHOT</div>
          <div class="stats-data">
            DATE: {{ 'snaphsot date' }} <br>
            TIME: {{ 'snaphsot time' }} <br>
            OTHER DATA... <br>
          </div>
        </div>
        <div class="avgs">
          <div class="stats-header">AVERAGES</div>
          <div class="stats-data">
            {{ 'avg. temp. last 24h' }} <br>
            {{ 'avg. temp. last 7d' }} <br>
            {{ 'avg. humid. last 24h' }} <br>
            {{ 'avg. humid. last 7d' }} <br>
          </div>
        </div>
      </div>
    </dialog>
    -->
  </Container>
</template>