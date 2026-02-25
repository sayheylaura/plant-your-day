export class ApiError extends Error {
  readonly status: number

  constructor(message: string, status: number) {
    super(message)
    this.name = 'ApiError'
    this.status = status
    Object.setPrototypeOf(this, ApiError.prototype)
  }
}

export function getErrorMessage(error: unknown): string {
  if (error instanceof ApiError) {
    switch (error.status) {
      case 0:
        return 'Your plants are lost in the forest. Please try again later.'
      case 404:
        return "We couldn't find your plants."
      case 500:
        return 'Your plants are lost in the forest. Please try again later.'
      default:
        return 'Your plants are lost in the forest. Please try again later.'
    }
  }
  return 'Your plants are lost in the forest. Please try again later.'
}
