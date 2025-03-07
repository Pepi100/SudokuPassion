import { NextResponse } from "next/server";
import fs from "fs";
import path from "path";

export async function GET(request: Request, { params }: { params: { id: string } }) {
    const { id } = await params; // ✅ Await params to resolve it properly

    const filePath = path.join(process.cwd(), "public", "puzzles.json");
    const puzzles = JSON.parse(fs.readFileSync(filePath, "utf-8"));

    const puzzle = puzzles.find((p: { id: string }) => p.id === id);

    if (!puzzle) {
        return NextResponse.json({ error: "Puzzle not found" }, { status: 404 });
    }

    return NextResponse.json(puzzle);
}
