"use client";

import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { API_BASE_URL, getErrorMessage, parseJson } from "@/lib/api";
import { getToken } from "@/lib/token";

type Product = {
  id: number;
  name: string;
  price: number;
  description?: string | null;
  quantity: number;
};

export default function ProductDetailPage() {
  const params = useParams();
  const router = useRouter();
  const id = Array.isArray(params.id) ? params.id[0] : params.id;
  const [product, setProduct] = useState<Product | null>(null);
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [description, setDescription] = useState("");
  const [quantity, setQuantity] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const loadProduct = async () => {
    if (!id) return;
    setLoading(true);
    setError("");
    try {
      const response = await fetch(`${API_BASE_URL}/products/${id}`);
      const data = await parseJson<Product & { detail?: string }>(response);
      if (!response.ok) {
        setError(getErrorMessage(data));
        return;
      }
      setProduct(data);
      setName(data.name || "");
      setPrice(String(data.price ?? ""));
      setDescription(data.description || "");
      setQuantity(String(data.quantity ?? ""));
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadProduct();
  }, [id]);

  const handleUpdate = async (event: React.FormEvent) => {
    event.preventDefault();
    setError("");
    const token = getToken();
    if (!token) {
      setError("Login required to update products.");
      return;
    }
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/products/${id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          name,
          price: Number(price),
          description: description || null,
          quantity: Number(quantity),
        }),
      });
      const data = await parseJson<Product & { detail?: string }>(response);
      if (!response.ok) {
        setError(getErrorMessage(data));
        return;
      }
      setProduct(data);
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async () => {
    const token = getToken();
    if (!token) {
      setError("Admin token required to delete products.");
      return;
    }
    if (!id) return;
    const confirmed = window.confirm("Delete this product? This cannot be undone.");
    if (!confirmed) return;
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/products/${id}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      if (!response.ok) {
        const data = await parseJson<{ detail?: string }>(response);
        setError(getErrorMessage(data));
        return;
      }
      router.push("/products");
    } catch (err) {
      setError(getErrorMessage(err instanceof Error ? err.message : undefined));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">
      <div className="flex flex-col gap-2">
        <p className="text-sm uppercase tracking-[0.3em] text-muted">Detail</p>
        <h1 className="text-3xl font-semibold">
          {product ? product.name : "Product"}
        </h1>
        <p className="text-sm text-muted">
          Update requires a login token. Delete requires admin role.
        </p>
      </div>

      {error ? <p className="text-sm text-accent">{error}</p> : null}
      {loading ? <p className="text-sm text-muted">Loading...</p> : null}

      {product ? (
        <div className="grid gap-6 lg:grid-cols-[1.1fr_0.9fr]">
          <div className="card rounded-3xl p-6">
            <h2 className="text-xl font-semibold">Current snapshot</h2>
            <div className="mt-4 space-y-3 text-sm text-muted">
              <p>
                <span className="font-semibold text-ink">ID:</span> {product.id}
              </p>
              <p>
                <span className="font-semibold text-ink">Price:</span> ${product.price.toFixed(2)}
              </p>
              <p>
                <span className="font-semibold text-ink">Quantity:</span> {product.quantity}
              </p>
              <p>
                <span className="font-semibold text-ink">Description:</span> {product.description || "None"}
              </p>
            </div>
            <button
              className="mt-6 rounded-full border border-accent/40 px-5 py-2 text-sm font-semibold text-accent transition hover:bg-accent hover:text-card"
              onClick={handleDelete}
              type="button"
            >
              Delete product
            </button>
          </div>
          <div className="card rounded-3xl p-6">
            <h2 className="text-xl font-semibold">Update product</h2>
            <form className="mt-4 space-y-4" onSubmit={handleUpdate}>
              <div className="space-y-2">
                <label className="text-sm font-medium" htmlFor="name">
                  Name
                </label>
                <input
                  className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40"
                  id="name"
                  onChange={(event) => setName(event.target.value)}
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
                    className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40"
                    id="price"
                    onChange={(event) => setPrice(event.target.value)}
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
                    className="w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40"
                    id="quantity"
                    onChange={(event) => setQuantity(event.target.value)}
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
                  className="min-h-[120px] w-full rounded-2xl border border-ink/20 bg-white/80 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sea/40"
                  id="description"
                  onChange={(event) => setDescription(event.target.value)}
                  value={description}
                />
              </div>
              <button
                className="btn-primary w-full rounded-2xl px-6 py-3 text-sm font-semibold shadow-soft transition hover:-translate-y-0.5"
                disabled={loading}
                type="submit"
              >
                {loading ? "Updating..." : "Update product"}
              </button>
            </form>
          </div>
        </div>
      ) : null}
    </div>
  );
}
