"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import { API_BASE_URL, getErrorMessage, parseJson } from "@/lib/api";
import { getToken } from "@/lib/token";

type Product = {
  id: number;
  name: string;
  price: number;
  description?: string | null;
  quantity: number;
};

const PAGE_SIZE = 8;

export default function ProductsPage() {
  const [items, setItems] = useState<Product[]>([]);
  const [search, setSearch] = useState("");
  const [skip, setSkip] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const token = useMemo(() => getToken(), []);

  const loadProducts = async () => {
    setLoading(true);
    setError("");
    try {
      const params = new URLSearchParams();
      params.set("skip", String(skip));
      params.set("limit", String(PAGE_SIZE));
      if (search) params.set("search", search);
      const response = await fetch(`${API_BASE_URL}/products?${params.toString()}`);
      const data = await parseJson<Product[]>(response);
      if (!response.ok) {
        setError(getErrorMessage(data as unknown as { detail?: string }));
        return;
      }
      setItems(Array.isArray(data) ? data : []);
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadProducts();
  }, [skip]);

  return (
    <div className="space-y-8">
      <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
        <div>
          <p className="text-sm uppercase tracking-[0.3em] text-muted">
            Catalog
          </p>
          <h1 className="text-3xl font-semibold sm:text-4xl">Products</h1>
          <p className="mt-2 text-sm text-muted">
            Browse inventory. Create and update require a login token.
          </p>
        </div>
        <div className="flex flex-col gap-3 sm:flex-row">
          <input
            className="w-full rounded-full border border-ink/20 bg-white/80 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40 sm:w-72"
            onChange={(event) => setSearch(event.target.value)}
            placeholder="Search by product name"
            value={search}
          />
          <button
            className="btn-outline rounded-full px-5 py-2 text-sm font-semibold transition hover:bg-ink hover:text-card"
            onClick={() => {
              setSkip(0);
              loadProducts();
            }}
            type="button"
          >
            Search
          </button>
        </div>
      </div>

      <div className="flex flex-wrap items-center gap-3 text-xs text-muted">
        <span className="rounded-full border border-ink/10 bg-white/70 px-3 py-1">
          Token: {token ? "active" : "missing"}
        </span>
        <Link className="text-ink underline" href="/login">
          Login
        </Link>
        <Link className="text-ink underline" href="/products/new">
          Create product
        </Link>
      </div>

      {error ? <p className="text-sm text-accent">{error}</p> : null}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
        {items.map((product) => (
          <Link
            className="card group rounded-3xl p-6 transition hover:-translate-y-1"
            href={`/products/${product.id}`}
            key={product.id}
          >
            <div className="flex items-center justify-between text-xs uppercase tracking-[0.2em] text-muted">
              <span>ID {product.id}</span>
              <span>{product.quantity} in stock</span>
            </div>
            <h3 className="mt-3 text-xl font-semibold">{product.name}</h3>
            <p className="mt-2 text-sm text-muted">
              {product.description || "No description provided."}
            </p>
            <div className="mt-4 flex items-center justify-between text-sm">
              <span className="font-semibold">${product.price.toFixed(2)}</span>
              <span className="text-muted group-hover:text-ink">View details</span>
            </div>
          </Link>
        ))}
      </div>

      {loading ? <p className="text-sm text-muted">Loading...</p> : null}

      <div className="flex items-center justify-between">
        <button
          className="btn-outline rounded-full px-5 py-2 text-sm font-semibold transition hover:bg-ink hover:text-card"
          disabled={skip === 0}
          onClick={() => setSkip(Math.max(0, skip - PAGE_SIZE))}
          type="button"
        >
          Previous
        </button>
        <button
          className="btn-outline rounded-full px-5 py-2 text-sm font-semibold transition hover:bg-ink hover:text-card"
          onClick={() => setSkip(skip + PAGE_SIZE)}
          type="button"
        >
          Next
        </button>
      </div>
    </div>
  );
}
