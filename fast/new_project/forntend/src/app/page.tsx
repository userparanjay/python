import Link from "next/link";

export default function Home() {
  return (
    <div className="space-y-12">
      <section className="grid gap-10 lg:grid-cols-[1.1fr_0.9fr]">
        <div className="space-y-6">
          <p className="text-sm uppercase tracking-[0.3em] text-muted">
            Inventory Command
          </p>
          <h1 className="text-4xl font-semibold sm:text-5xl lg:text-6xl">
            Shape your product catalog with clarity and speed.
          </h1>
          <p className="text-lg text-muted">
            This console talks to your FastAPI backend to manage products,
            authenticate teams, and keep inventory live. Start by creating an
            account or jump into the catalog.
          </p>
          <div className="flex flex-wrap gap-3">
            <Link
              className="btn-primary rounded-full px-6 py-3 text-sm font-semibold shadow-soft transition hover:-translate-y-0.5"
              href="/products"
            >
              Explore Products
            </Link>
            <Link
              className="btn-outline rounded-full px-6 py-3 text-sm font-semibold text-ink transition hover:bg-ink hover:text-card"
              href="/signup"
            >
              Create Account
            </Link>
          </div>
        </div>
        <div className="card rounded-3xl p-6 sm:p-8">
          <div className="space-y-4">
            <div className="flex items-center justify-between text-sm text-muted">
              <span>Connected Routes</span>
              <span>FastAPI</span>
            </div>
            <div className="space-y-3">
              {[
                "POST /signup",
                "POST /login",
                "PUT /user/update",
                "POST /reset-password",
                "POST /reset-password/confirm",
                "GET /products",
                "POST /products",
                "GET /products/{id}",
                "PUT /products/{id}",
                "DELETE /products/{id}",
              ].map((route) => (
                <div
                  key={route}
                  className="flex items-center justify-between rounded-2xl border border-ink/10 bg-white/70 px-4 py-3"
                >
                  <span className="text-sm font-medium text-ink">{route}</span>
                  <span className="text-xs uppercase tracking-[0.2em] text-muted">
                    ready
                  </span>
                </div>
              ))}
            </div>
            <p className="text-xs text-muted">
              Use the login token to unlock create, update, and delete actions.
            </p>
          </div>
        </div>
      </section>

      <section className="grid gap-6 md:grid-cols-3">
        {[
          {
            title: "Live search",
            copy: "Filter inventory by name using the built-in search query.",
          },
          {
            title: "Role-aware actions",
            copy: "Admin roles can delete products; standard users manage updates.",
          },
          {
            title: "API ready",
            copy: "All UI panels mirror your current FastAPI endpoints.",
          },
        ].map((item) => (
          <div key={item.title} className="card rounded-3xl p-6">
            <h3 className="text-lg font-semibold">{item.title}</h3>
            <p className="mt-2 text-sm text-muted">{item.copy}</p>
          </div>
        ))}
      </section>
    </div>
  );
}
