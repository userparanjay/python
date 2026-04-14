"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { API_BASE_URL, getErrorMessage, parseJson } from "@/lib/api";
import { getToken } from "@/lib/token";

type UserResponse = {
  id: number;
  username: string;
  email: string;
  is_active: boolean;
  created_at: string;
  profile_picture?: string | null;
};

const resolveProfileImage = (filename?: string | null) => {
  if (!filename) return null;
  const base = API_BASE_URL.replace(/\/+$/, "");
  return `${base}/uploads/profile_pictures/${encodeURIComponent(filename)}`;
};

export default function ProfilePage() {
  const [username, setUsername] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [user, setUser] = useState<UserResponse | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [isEditing, setIsEditing] = useState(false);
  const [hasToken, setHasToken] = useState(false);
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [passwordSuccess, setPasswordSuccess] = useState("");
  const [passwordLoading, setPasswordLoading] = useState(false);

  const fetchMe = async () => {
    const token = getToken();
    if (!token) return;
    setLoading(true);
    setError("");
    try {
      const response = await fetch(`${API_BASE_URL}/user/me`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await parseJson<UserResponse & { detail?: string }>(response);
      if (!response.ok) {
        setError(getErrorMessage(data));
        return;
      }
      setUser(data);
      setUsername(data.username || "");
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError("");
    const token = getToken();
    if (!token) {
      setError("Login required to update your profile.");
      return;
    }

    const formData = new FormData();
    if (username) formData.append("username", username);
    if (file) formData.append("profile_picture", file);

    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/user/update`, {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        body: formData,
      });
      const data = await parseJson<UserResponse & { detail?: string }>(response);
      if (!response.ok) {
        setError(getErrorMessage(data));
        return;
      }
      setUser(data);
      setIsEditing(false);
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  const handleChangePassword = async (event: React.FormEvent) => {
    event.preventDefault();
    setPasswordError("");
    setPasswordSuccess("");
    const token = getToken();
    if (!token) {
      setPasswordError("Login required to change your password.");
      return;
    }
    if (!oldPassword || !newPassword) {
      setPasswordError("Please fill out both password fields.");
      return;
    }
    if (newPassword !== confirmPassword) {
      setPasswordError("New password and confirmation do not match.");
      return;
    }
    setPasswordLoading(true);
    try {
      const params = new URLSearchParams();
      params.set("old_password", oldPassword);
      params.set("new_password", newPassword);
      const response = await fetch(`${API_BASE_URL}/change-password?${params.toString()}`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await parseJson<{ message?: string; detail?: string }>(response);
      if (!response.ok) {
        setPasswordError(getErrorMessage(data));
        return;
      }
      setPasswordSuccess(data.message || "Password updated.");
      setOldPassword("");
      setNewPassword("");
      setConfirmPassword("");
    } catch (err) {
      setPasswordError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setPasswordLoading(false);
    }
  };

  useEffect(() => {
    const token = getToken();
    setHasToken(Boolean(token));
    if (token) {
      fetchMe();
    }
  }, []);

  return (
    <div className="mx-auto max-w-2xl space-y-6">
      <div>
        <p className="text-sm uppercase tracking-[0.3em] text-muted">Profile</p>
        <h1 className="text-3xl font-semibold">Update profile</h1>
        <p className="mt-2 text-sm text-muted">
          Update username and profile picture via `PUT /user/update`.
        </p>
      </div>

      {!hasToken ? (
        <div className="card rounded-3xl p-6">
          <h2 className="text-xl font-semibold">Login required</h2>
          <p className="mt-2 text-sm text-muted">
            Sign in to view and edit your profile information.
          </p>
          <Link
            className="btn-primary mt-4 inline-flex rounded-full px-5 py-2 text-sm font-semibold shadow-soft transition hover:-translate-y-0.5"
            href="/login"
          >
            Go to login
          </Link>
        </div>
      ) : null}

      {hasToken ? (
        <div className="card rounded-3xl p-6">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div className="flex items-center gap-4">
            {resolveProfileImage(user?.profile_picture) ? (
              <img
                alt="Profile from backend"
                className="h-20 w-20 rounded-3xl border border-ink/10 object-cover"
                src={resolveProfileImage(user?.profile_picture) ?? undefined}
              />
            ) : (
              <div className="flex h-20 w-20 items-center justify-center rounded-3xl border border-ink/10 bg-white/70 text-xl font-semibold">
                {user?.username?.slice(0, 2).toUpperCase() || "US"}
              </div>
            )}
            <div>
              <p className="text-sm text-muted">Signed in as</p>
              <h2 className="text-2xl font-semibold">{user?.username || "Unknown"}</h2>
              <p className="text-sm text-muted">{user?.email || "No email"}</p>
            </div>
          </div>
          <button
            className="flex items-center gap-2 rounded-full border border-ink/20 px-4 py-2 text-sm font-semibold transition hover:bg-ink hover:text-card"
            onClick={() => setIsEditing((prev) => !prev)}
            type="button"
          >
            <span>Edit</span>
            <svg
              aria-hidden="true"
              className="h-4 w-4"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              viewBox="0 0 24 24"
            >
              <path d="M12 20h9" />
              <path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5z" />
            </svg>
          </button>
        </div>
      </div>
      ) : null}

      {isEditing ? (
        <div className="card rounded-3xl p-8">
          <form className="space-y-4" onSubmit={handleSubmit}>
            <div className="space-y-2">
              <label className="text-sm font-medium" htmlFor="username">
                Username
              </label>
              <input
                className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/40"
                id="username"
                onChange={(event) => setUsername(event.target.value)}
                placeholder="Update username"
                type="text"
                value={username}
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium" htmlFor="profile_picture">
                Profile picture
              </label>
              <input
                className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm"
                id="profile_picture"
                accept="image/*"
                onChange={(event) => {
                  const selected = event.target.files?.[0] || null;
                  setFile(selected);
                  if (selected) {
                    const url = URL.createObjectURL(selected);
                    setPreviewUrl((prev) => {
                      if (prev) URL.revokeObjectURL(prev);
                      return url;
                    });
                  } else {
                    setPreviewUrl((prev) => {
                      if (prev) URL.revokeObjectURL(prev);
                      return null;
                    });
                  }
                }}
                type="file"
              />
            </div>
            {previewUrl ? (
              <div className="card rounded-2xl border border-ink/10 bg-white/70 p-4">
                <p className="text-xs uppercase tracking-[0.2em] text-muted">
                  Image preview
                </p>
                <img
                  alt="Selected profile preview"
                  className="mt-3 h-40 w-40 rounded-3xl border border-ink/10 object-cover"
                  src={previewUrl}
                />
              </div>
            ) : null}
            <button
              className="btn-primary w-full rounded-2xl px-6 py-3 text-sm font-semibold shadow-soft transition hover:-translate-y-0.5"
              disabled={loading}
              type="submit"
            >
              {loading ? "Updating..." : "Update profile"}
            </button>
          </form>
        </div>
      ) : null}

      {hasToken ? (
        <div className="card rounded-3xl p-8">
          <h2 className="text-xl font-semibold">Change password</h2>
          <p className="mt-2 text-sm text-muted">
            Uses `POST /change-password` with your current token.
          </p>
          <form className="mt-6 space-y-4" onSubmit={handleChangePassword}>
            <div className="space-y-2">
              <label className="text-sm font-medium" htmlFor="old_password">
                Old password
              </label>
              <input
                className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40"
                id="old_password"
                onChange={(event) => setOldPassword(event.target.value)}
                required
                type="password"
                value={oldPassword}
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium" htmlFor="new_password">
                New password
              </label>
              <input
                className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40"
                id="new_password"
                onChange={(event) => setNewPassword(event.target.value)}
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
                onChange={(event) => setConfirmPassword(event.target.value)}
                required
                type="password"
                value={confirmPassword}
              />
            </div>
            {passwordError ? <p className="text-sm text-accent">{passwordError}</p> : null}
            {passwordSuccess ? <p className="text-sm text-sea">{passwordSuccess}</p> : null}
            <button
              className="btn-primary w-full rounded-2xl px-6 py-3 text-sm font-semibold shadow-soft transition hover:-translate-y-0.5"
              disabled={passwordLoading}
              type="submit"
            >
              {passwordLoading ? "Updating..." : "Update password"}
            </button>
          </form>
        </div>
      ) : null}

      {error ? <p className="text-sm text-accent">{error}</p> : null}
    </div>
  );
}
