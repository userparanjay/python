export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export type ApiError = {
  detail?: string;
  message?: string;
};

export async function parseJson<T>(response: Response): Promise<T> {
  const text = await response.text();
  if (!text) {
    return {} as T;
  }
  return JSON.parse(text) as T;
}

export function getErrorMessage(error: ApiError | string | null | undefined) {
  if (!error) return "Unexpected error";
  if (typeof error === "string") return error;
  return error.detail || error.message || "Unexpected error";
}
