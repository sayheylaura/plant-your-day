<script setup lang="ts">
import { useQuery } from '@tanstack/vue-query'

import { getPlants } from '@/api/plants'
import { getErrorMessage } from '@/utils/errorHandling'

const { data, status, error, refetch } = useQuery({
  queryKey: ['plants'],
  queryFn: getPlants,
  refetchOnWindowFocus: false,
})
</script>

<template>
  <main>
    <p v-if="status === 'pending'" class="text-center text-lg" role="status" aria-live="polite">
      Growing plants...
    </p>
    <div v-if="status === 'error'" class="text-center" role="alert" aria-live="assertive">
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
    <ul
      v-else-if="data && data.length > 0"
      class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4"
    >
      <li
        v-for="plant in data"
        :key="plant.id"
        class="border border-gray-200 p-4 rounded-md hover:bg-gray-50"
      >
        <RouterLink :to="`/plants/${plant.id}`" class="block">
          <article>
            <h2 class="text-lg font-bold">{{ plant.name }}</h2>
            <p class="text-sm text-gray-500">{{ plant.species }}</p>
          </article>
        </RouterLink>
      </li>
    </ul>
    <p v-else class="text-center text-lg">
      No plants found. Maybe you should
      <RouterLink to="/plants/create" class="text-green-500 hover:text-green-600"
        >plant one</RouterLink
      >?
    </p>
  </main>
</template>
