"use client";

import { useState, useEffect } from "react";
import { useParams } from "next/navigation";
import styles from './page.module.css'; // Import the CSS module

export default function PuzzlePage() {
    const params = useParams();
    const [grid, setGrid] = useState<(number | null)[][] | null>(null);
    const [puzzleName, setPuzzleName] = useState<string>("");

    useEffect(() => {
        async function fetchPuzzle() {
            if (!params.id) return;

            try {
                const response = await fetch(`/api/puzzles/${params.id}`);
                if (!response.ok) {
                    throw new Error("Puzzle not found");
                }
                const puzzle = await response.json();
                setGrid(puzzle.grid);
                setPuzzleName(puzzle.name);
            } catch (error) {
                console.error(error);
            }
        }

        fetchPuzzle();
    }, [params.id]);

    const handleChange = (rowIndex: number, colIndex: number, value: string) => {
        if (!grid) return;
        const newGrid = grid.map((row, rIdx) =>
            row.map((num, cIdx) =>
                rIdx === rowIndex && cIdx === colIndex ? (value ? parseInt(value) || null : null) : num
            )
        );
        setGrid(newGrid);
    };

    if (!grid) {
        return <p>Loading...</p>;
    }

    return (
        <div className={styles.container}>
            <h2 className={styles.title}>{puzzleName}</h2>
            <h3 className={styles.subtitle}>Sudoku Grid:</h3>
            <div style={{ display: "flex", justifyContent: "center" }}>
                <table className={styles.table}>
                    <tbody>
                        {grid.map((row, rowIndex) => (
                            <tr key={rowIndex}>
                                {row.map((num, colIndex) => (
                                    <td
                                        key={colIndex}
                                        className={`${styles.cell} ${num !== null ? styles.filled : ''}`}
                                    >
                                        {num !== null ? (
                                            num
                                        ) : (
                                            <input
                                                type="text"
                                                maxLength={1}
                                                className={styles.input}
                                                onChange={(e) => handleChange(rowIndex, colIndex, e.target.value)}
                                            />
                                        )}
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
