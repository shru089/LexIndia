import { Inter, Playfair_Display } from "next/font/google";
import Navbar from "@/components/Navbar";
import HelpDrawer from "@/components/HelpDrawer";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const playfair = Playfair_Display({
  variable: "--font-playfair",
  subsets: ["latin"],
});

export const metadata = {
  title: "Lex India - Legal AI Companion",
  description: "Democratize access to legal knowledge across India by removing cost, language, and literacy barriers.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={`${inter.variable} ${playfair.variable}`}>
      <body>
        <Navbar />
        <main style={{ flex: 1 }}>{children}</main>
        <HelpDrawer />
        
        {/* Footer */}
        <footer style={{
          background: 'var(--neutral-color)',
          padding: '1.5rem 4rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          fontSize: '0.85rem',
          color: 'var(--text-secondary)'
        }}>
          <div>
            <span style={{ fontFamily: 'var(--font-playfair)', fontWeight: 'bold', fontSize: '1.1rem', color: 'var(--text-primary)' }}>Lex India</span>
            <br />
            © 2026 Lex India. Professional Legal Technology.
          </div>
          <div style={{ display: 'flex', gap: '2rem' }}>
            <a href="#">Terms of Service</a>
            <a href="#">Privacy Policy</a>
          </div>
          <div style={{ maxWidth: '300px', textAlign: 'right', opacity: 0.8 }}>
            Disclaimer: AI-generated content is for research purposes only and does not constitute legal advice.
          </div>
        </footer>
      </body>
    </html>
  );
}
