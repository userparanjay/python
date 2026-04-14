import type { Metadata } from "next";
import { Fraunces, Space_Grotesk } from "next/font/google";
import "./globals.css";
import TopNav from "@/components/TopNav";

const displayFont = Fraunces({
  variable: "--font-display",
  subsets: ["latin"],
});

const bodyFont = Space_Grotesk({
  variable: "--font-body",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Product Console",
  description: "Frontend for the FastAPI product service",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${displayFont.variable} ${bodyFont.variable} antialiased`}>
        <div className="min-h-screen bg-page text-ink">
          <div className="pointer-events-none fixed inset-0 overflow-hidden">
            <div className="absolute -top-40 right-[-10%] h-[420px] w-[420px] rounded-full bg-accent/20 blur-[120px]" />
            <div className="absolute bottom-[-15%] left-[-5%] h-[520px] w-[520px] rounded-full bg-sea/20 blur-[140px]" />
            <div className="absolute inset-0 bg-grid opacity-[0.35]" />
          </div>
          <div className="relative z-10">
            <TopNav />
            <main className="mx-auto w-full max-w-6xl px-6 pb-20 pt-10 sm:px-10">
              {children}
            </main>
            <footer className="border-t border-ink/10 py-8">
              <div className="mx-auto flex w-full max-w-6xl flex-col gap-2 px-6 text-sm text-ink/70 sm:flex-row sm:items-center sm:justify-between sm:px-10">
                <span>Product Console</span>
                <span>FastAPI + Next.js + Tailwind</span>
              </div>
            </footer>
          </div>
        </div>
      </body>
    </html>
  );
}
