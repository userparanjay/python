"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { clearToken, getToken } from "@/lib/token";

export default function TopNav() {
  const [token, setToken] = useState<string | null>(null);

  useEffect(() => {
    setToken(getToken());
  }, []);

  const handleLogout = () => {
    clearToken();
    setToken(null);
  };

  return (
    <header className="border-b border-ink/10 bg-page/80 backdrop-blur">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-4 px-6 py-6 sm:flex-row sm:items-center sm:justify-between sm:px-10">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-2xl bg-ink text-card">PC</div>
          <div>
            <p className="text-lg font-semibold">Product Console</p>
            <p className="text-sm text-muted">FastAPI inventory workspace</p>
          </div>
        </div>
        <nav className="flex flex-wrap items-center gap-3 text-sm">
          <Link className="rounded-full px-4 py-2 transition hover:bg-ink/10" href="/">
            Overview
          </Link>
          <Link className="rounded-full px-4 py-2 transition hover:bg-ink/10" href="/products">
            Products
          </Link>
          <Link className="rounded-full px-4 py-2 transition hover:bg-ink/10" href="/products/new">
            New Product
          </Link>
          <Link className="rounded-full px-4 py-2 transition hover:bg-ink/10" href="/profile">
            Profile
          </Link>
          <Link className="rounded-full px-4 py-2 transition hover:bg-ink/10" href="/login">
            Login
          </Link>
          <Link className="rounded-full px-4 py-2 transition hover:bg-ink/10" href="/signup">
            Sign Up
          </Link>
          {token ? (
            <button
              className="rounded-full border border-ink/20 px-4 py-2 text-ink transition hover:bg-ink hover:text-card"
              onClick={handleLogout}
              type="button"
            >
              Logout
            </button>
          ) : null}
        </nav>
      </div>
    </header>
  );
}
