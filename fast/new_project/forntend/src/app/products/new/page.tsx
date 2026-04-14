"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { API_BASE_URL, getErrorMessage, parseJson } from "@/lib/api";
import { getToken } from "@/lib/token";

type ProductPayload = {
  name: string;
  price: number;
  description?: string | null;
  quantity: number;
};

export default function NewProductPage() {
  const router = useRouter();
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [description, setDescription] = useState("");
  const [quantity, setQuantity] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError("");
    const token = getToken();
    if (!token) {
      setError("Login required to create products.");
      return;
    }
    const payload: ProductPayload = {
      name,
      price: Number(price),
      description: description || null,
      quantity: Number(quantity),
    };
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/products`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(payload),
      });
      const data = await parseJson<{ id?: number; detail?: string }>(response);
      if (!response.ok) {
        setError(getErrorMessage(data));
        return;
      }
      if (data.id) {
        router.push(`/products/${data.id}`);
      } else {
        router.push("/products");
      }
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto max-w-2xl space-y-6">
      <div>
        <p className="text-sm uppercase tracking-[0.3em] text-muted">Create</p>
        <h1 className="text-3xl font-semibold">New Product</h1>
        <p className="mt-2 text-sm text-muted">
          Requires a valid login token. Fields must match the FastAPI schema.
        </p>
      </div>
      <div className="card rounded-3xl p-8">
        <form className="space-y-4" onSubmit={handleSubmit}>
          <div className="space-y-2">
            <label className="text-sm font-medium" htmlFor="name">
              Name
            </label>
            <input
              className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/40"
              id="name"
              onChange={(event) => setName(event.target.value)}
              placeholder="iPhone 15"
              required
              type="text"
              value={name}
            />
          </div>
          <div className="grid gap-4 sm:grid-cols-2">
            <div className="space-y-2">
              <label className="text-sm font-medium" htmlFor="price">
                Price
              </label>
              <input
                className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/40"
                id="price"
                onChange={(event) => setPrice(event.target.value)}
                placeholder="999.99"
                required
                type="number"
                min="0"
                step="0.01"
                value={price}
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium" htmlFor="quantity">
                Quantity
              </label>
              <input
                className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/40"
                id="quantity"
                onChange={(event) => setQuantity(event.target.value)}
                placeholder="10"
                required
                type="number"
                min="0"
                step="1"
                value={quantity}
              />
            </div>
          </div>
          <div className="space-y-2">
            <label className="text-sm font-medium" htmlFor="description">
              Description
            </label>
            <textarea
              className="min-h-[120px] w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-accent/40"
              id="description"
              onChange={(event) => setDescription(event.target.value)}
              placeholder="Apple smartphone with A16 chip"
              value={description}
            />
          </div>
          {error ? <p className="text-sm text-accent">{error}</p> : null}
          <button
            className="btn-primary w-full rounded-2xl px-6 py-3 text-sm font-semibold shadow-soft transition hover:-translate-y-0.5"
            disabled={loading}
            type="submit"
          >
            {loading ? "Saving..." : "Create product"}
          </button>
        </form>
      </div>
    </div>
  );
}
