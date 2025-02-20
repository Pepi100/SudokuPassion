import type { Metadata } from "next";
import "./globals.css";



export const metadata: Metadata = {
  title: "Sudoku Passion",
  description: "TODO",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <header>
          <p>Header</p>
        </header>
        {children}
        <footer>
          footer
        </footer>
      </body>
    </html>
  );
}
