<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useQuery } from '@tanstack/vue-query'

import { getPlantById } from '@/api/plants'
import { getErrorMessage } from '@/utils/errorHandling'

const route = useRoute()

const plantId = computed(() => {
  const id = route.params.id
  if (!id) return undefined
  return Array.isArray(id) ? id[0] : id
})

const hasValidId = computed(() => {
  const id = plantId.value
  return id != null && id !== '' && (typeof id === 'number' ? true : !Number.isNaN(Number(id)))
})

const {
  data: plant,
  status,
  error,
  refetch,
} = useQuery({
  queryKey: ['plant', plantId],
  queryFn: () => getPlantById(plantId.value!),
  enabled: hasValidId,
})
</script>

<template>
  <main>
    <RouterLink
      to="/"
      class="bg-green-500 hover:bg-green-600 text-white text-xs p-2 rounded-md mb-4 w-fit"
    >
      Go back to your plants
    </RouterLink>

    <div v-if="!hasValidId" class="text-center text-lg" role="alert" aria-live="assertive">
      <p class="text-lg">Plant not found.</p>
      <RouterLink to="/" class="text-green-500 hover:text-green-600">
        Go back to your plants
      </RouterLink>
    </div>

    <p
      v-else-if="status === 'pending' && hasValidId"
      class="text-center text-lg"
      role="status"
      aria-live="polite"
    >
      Growing your plant...
    </p>

    <!-- TODO: improve error handling for different error types-->
    <div v-else-if="status === 'error'" class="text-center" role="alert" aria-live="assertive">
      <p class="text-lg">
        {{ getErrorMessage(error) }}
      </p>
      <button
        type="button"
        @click="refetch()"
        class="text-green-500 hover:text-green-600 cursor-pointer"
      >
        Try again
      </button>
    </div>

    <div v-else-if="plant">
      <article class="p-20">
        <h2 class="text-2xl font-bold">{{ plant.name }}</h2>
        <p class="text-lg">Species: {{ plant.species }}</p>
        <p v-if="plant.notes" class="text-lg">{{ plant.notes }}</p>
      </article>
    </div>
  </main>
</template>
