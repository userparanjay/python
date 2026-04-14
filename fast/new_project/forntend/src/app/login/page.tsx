"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { API_BASE_URL, getErrorMessage, parseJson } from "@/lib/api";
import { clearToken, setToken } from "@/lib/token";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError("");
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      const data = await parseJson<{ access_token?: string; message?: string; detail?: string }>(
        response
      );
      if (!response.ok) {
        setError(getErrorMessage(data));
        return;
      }
      if (data.access_token) {
        setToken(data.access_token);
        router.push("/products");
      } else {
        setError("Token missing in response.");
      }
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto max-w-xl">
      <div className="card rounded-3xl p-8">
        <h1 className="text-3xl font-semibold">Welcome back</h1>
        <p className="mt-2 text-sm text-muted">
          Login to unlock inventory controls.
        </p>
        <form className="mt-8 space-y-4" onSubmit={handleSubmit}>
          <div className="space-y-2">
            <label className="text-sm font-medium" htmlFor="email">
              Email
            </label>
            <input
              className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/40"
              id="email"
              name="email"
              onChange={(event) => setEmail(event.target.value)}
              placeholder="you@company.com"
              required
              type="email"
              value={email}
            />
          </div>
          <div className="space-y-2">
            <label className="text-sm font-medium" htmlFor="password">
              Password
            </label>
            <input
              className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/40"
              id="password"
              name="password"
              onChange={(event) => setPassword(event.target.value)}
              placeholder="Enter your password"
              required
              type="password"
              value={password}
            />
          </div>
          {error ? <p className="text-sm text-accent">{error}</p> : null}
          <button
            className="btn-primary w-full rounded-2xl px-6 py-3 text-sm font-semibold shadow-soft transition hover:-translate-y-0.5"
            disabled={loading}
            type="submit"
          >
            {loading ? "Signing in..." : "Sign in"}
          </button>
        </form>
        <div className="mt-4 flex flex-col items-center gap-2 text-sm text-muted">
          <a className="underline" href="/forgot-password">
            Forgot password?
          </a>
          <button
            className="rounded-full border border-ink/20 px-4 py-2 text-xs font-semibold text-ink transition hover:bg-ink hover:text-card"
            onClick={() => clearToken()}
            type="button"
          >
            Logout
          </button>
        </div>
      </div>
    </div>
  );
}
