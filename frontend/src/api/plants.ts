import type { Plant } from '@/types'

import { ApiError } from '@/utils/errorHandling'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

function checkApiBaseUrl() {
  if (!API_BASE_URL) {
    const errorMessage = 'VITE_API_BASE_URL is not defined. Please set it in your .env file.'
    console.error(errorMessage)
    throw new ApiError(errorMessage, 0)
  }
}

export async function getPlants(): Promise<Plant[]> {
  checkApiBaseUrl()

  const url = `${API_BASE_URL}/plants`
  const response = await fetch(url)

  if (!response.ok) {
    const status = response.status
    const statusText = response.statusText || `HTTP ${status}`
    throw new ApiError(`Failed to fetch plants: ${statusText}`, status)
  }

  const data = await response.json()
  return data
}

export async function getPlantById(id: string): Promise<Plant> {
  checkApiBaseUrl()

  const url = `${API_BASE_URL}/plants/${id}`
  const response = await fetch(url)

  if (!response.ok) {
    const status = response.status
    const statusText = response.statusText || `HTTP ${status}`
    throw new ApiError(`Failed to fetch plant by ID ${id}: ${statusText}`, status)
  }

  const data = await response.json()
  return data
}
