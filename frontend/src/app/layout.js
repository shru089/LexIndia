import AppShell from "@/components/layout/AppShell";
import "./globals.css";

export const metadata = {
  title: "Lex India | Legal intelligence for citizens and advocates",
  description:
    "A legal intelligence platform for India that explains legal problems in plain language, surfaces relevant law, and connects users with verified human help.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <AppShell>{children}</AppShell>
      </body>
    </html>
  );
}
