"use client";

import { useEffect, useMemo, useState } from "react";
import { API_BASE_URL, getErrorMessage, parseJson } from "@/lib/api";

export default function ResetPasswordConfirmPage() {
  const [token, setToken] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (typeof window === "undefined") return;
    const params = new URLSearchParams(window.location.search);
    const tokenParam = params.get("token");
    if (tokenParam) {
      setToken(tokenParam);
    }
  }, []);

  const isTokenMissing = useMemo(() => !token, [token]);

  // Token validation happens on submit via /reset-password/confirm.

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError("");
    setSuccess("");
    if (!token) {
      setError("Reset token is missing.");
      return;
    }
    if (!newPassword) {
      setError("Please enter a new password.");
      return;
    }
    if (newPassword !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }
    setLoading(true);
    try {
      const params = new URLSearchParams();
      params.set("token", token);
      params.set("new_password", newPassword);
      const response = await fetch(
        `${API_BASE_URL}/reset-password/confirm?${params.toString()}`,
        { method: "POST" }
      );
      const data = await parseJson<{ message?: string; detail?: string }>(response);
      if (!response.ok) {
        setError(getErrorMessage(data));
        return;
      }
      setSuccess(data.message || "Password reset successfully.");
      setNewPassword("");
      setConfirmPassword("");
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto max-w-xl">
      <div className="card rounded-3xl p-8">
        <h1 className="text-3xl font-semibold">Reset password</h1>
        <p className="mt-2 text-sm text-muted">
          Set a new password for your account.
        </p>
        {isTokenMissing ? (
          <p className="mt-4 text-sm text-accent">
            Token missing. Please open the reset link from your email.
          </p>
        ) : null}
        <form className="mt-8 space-y-4" onSubmit={handleSubmit}>
          <div className="space-y-2">
            <label className="text-sm font-medium" htmlFor="new_password">
              New password
            </label>
            <input
              className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40"
              id="new_password"
              name="new_password"
              onChange={(event) => setNewPassword(event.target.value)}
              placeholder="Enter a new password"
              required
              type="password"
              value={newPassword}
            />
          </div>
          <div className="space-y-2">
            <label className="text-sm font-medium" htmlFor="confirm_password">
              Confirm new password
            </label>
            <input
              className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40"
              id="confirm_password"
              name="confirm_password"
              onChange={(event) => setConfirmPassword(event.target.value)}
              placeholder="Re-enter your new password"
              required
              type="password"
              value={confirmPassword}
            />
          </div>
          {error ? <p className="text-sm text-accent">{error}</p> : null}
          {success ? <p className="text-sm text-sea">{success}</p> : null}
          <button
            className="btn-primary w-full rounded-2xl px-6 py-3 text-sm font-semibold shadow-soft transition hover:-translate-y-0.5"
            disabled={loading || isTokenMissing}
            type="submit"
          >
            {loading ? "Updating..." : "Reset password"}
          </button>
        </form>
      </div>
    </div>
  );
}
