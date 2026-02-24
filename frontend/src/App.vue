<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header class="py-6 px-10 flex justify-between items-center">
    <h1 class="text-2xl font-bold mb-4 lg:text-4xl">
      <RouterLink to="/">Plant Your Day 🪴</RouterLink>
    </h1>
    <nav class="flex gap-4">
      <RouterLink to="/">Dashboard</RouterLink>
      <RouterLink to="/plants/create">Add plant</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>
