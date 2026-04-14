"use client";

import { useState } from "react";
import { API_BASE_URL, getErrorMessage, parseJson } from "@/lib/api";

export default function ForgotPasswordPage() {
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError("");
    setSuccess("");
    setLoading(true);
    try {
      const params = new URLSearchParams();
      params.set("email", email);
      const response = await fetch(`${API_BASE_URL}/reset-password?${params.toString()}`, {
        method: "POST",
      });
      const data = await parseJson<{ message?: string; detail?: string }>(response);
      if (!response.ok) {
        setError(getErrorMessage(data));
        return;
      }
      setSuccess(data.message || "Reset link sent. Check your email.");
      setEmail("");
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto max-w-xl">
      <div className="card rounded-3xl p-8">
        <h1 className="text-3xl font-semibold">Forgot your password?</h1>
        <p className="mt-2 text-sm text-muted">
          Enter your email and we will send you a reset link.
        </p>
        <form className="mt-8 space-y-4" onSubmit={handleSubmit}>
          <div className="space-y-2">
            <label className="text-sm font-medium" htmlFor="email">
              Email
            </label>
            <input
              className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40"
              id="email"
              name="email"
              onChange={(event) => setEmail(event.target.value)}
              placeholder="you@company.com"
              required
              type="email"
              value={email}
            />
          </div>
          {error ? <p className="text-sm text-accent">{error}</p> : null}
          {success ? <p className="text-sm text-sea">{success}</p> : null}
          <button
            className="btn-primary w-full rounded-2xl px-6 py-3 text-sm font-semibold shadow-soft transition hover:-translate-y-0.5"
            disabled={loading}
            type="submit"
          >
            {loading ? "Sending..." : "Send reset link"}
          </button>
        </form>
      </div>
    </div>
  );
}
