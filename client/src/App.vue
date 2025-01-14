<template>
  <router-view ></router-view>
  <!-- <router-view :key="route.fullPath"></router-view> -->
</template>

<script  setup>
import { useRoute } from 'vue-router'
    const route = useRoute()
</script>

<style>
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
</style>
