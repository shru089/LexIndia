"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { primaryNav } from "@/lib/constants/site";

export default function TopNav() {
  const pathname = usePathname();

  return (
    <div className="top-nav-wrap">
      <nav className="top-nav">
        <Link href="/" className="brand-mark">
          <span className="brand-seal">LI</span>
          <span className="brand-copy">
            <span className="brand-title">Lex India</span>
            <span className="brand-subtitle">Explain the law. Find the path.</span>
          </span>
        </Link>

        <div className="nav-links">
          {primaryNav.map((item) => {
            const active =
              pathname === item.href ||
              (item.href !== "/" && pathname.startsWith(item.href));

            return (
              <Link
                key={item.href}
                href={item.href}
                className={`nav-link${active ? " active" : ""}`}
              >
                {item.label}
              </Link>
            );
          })}
        </div>

        <div className="nav-actions">
          <Link href="/citizen/analyze" className="nav-pill">
            Upload or describe
          </Link>
          <Link href="/lawyers" className="btn-primary">
            Find lawyer
          </Link>
        </div>
      </nav>
    </div>
  );
}
