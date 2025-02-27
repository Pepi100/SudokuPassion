import fs from "fs";
import path from "path";
import { notFound } from "next/navigation"; // Import the 404 function

export default function PuzzlePage({ params }: { params: { id: string } }) {
    const filePath = path.join(process.cwd(), "public", "puzzles.json");
    const puzzles = JSON.parse(fs.readFileSync(filePath, "utf-8"));
    const puzzle = puzzles.find((p: { id: string }) => p.id === params.id);

    if (!puzzle) {
        notFound();
    }

    return (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
            <h2>{puzzle.name}</h2>
            <h3>Sudoku Grid:</h3>
            <div style={{ display: "flex", justifyContent: "center" }}>
                <table style={{ borderCollapse: "collapse" }}>
                    <tbody>
                        {puzzle.grid.map((row: number[], rowIndex: number) => (
                            <tr key={rowIndex}>
                                {row.map((num: number | null, colIndex: number) => (
                                    <td
                                        key={colIndex}
                                        style={{
                                            border: "1px solid black",
                                            width: "40px",
                                            height: "40px",
                                            textAlign: "center",
                                            verticalAlign: "middle",
                                            fontSize: "18px",
                                            backgroundColor: num === null ? "#f0f0f0" : "white",
                                            color: num !== null ? "black" : "gray",
                                        }}
                                    >
                                        {num !== null ? num : ""}
                                    </td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

