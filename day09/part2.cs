using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace day09
{
    public class Bridge_part2
    {
        // Setup a 2 dimensional array the size of the forest.
        const int MROWS = 999;
        const int MCOLS = 999;
        const int NUMKNOTS = 10;
        const int KNOTSTART = 499;

        int[,] grid = new int[MROWS, MCOLS];

        public class Knot
        {
            public int x;
            public int y;

            public Knot(int row, int col)
            {
                x = row;
                y = col;
            }
        }

        Knot[] knots = new Knot[10];

        public Bridge_part2()
        {
            // Initialize the starting point of all 10 knots
            for (int i = 0; i < NUMKNOTS; i++)
            {
                knots[i] = new Knot(KNOTSTART, KNOTSTART);
            }
        }
        
        public int spotsvisited()
        {
            int cnt = 0;
            for (int row = 0; row < MROWS; row++)
            {
                for (int col = 0; col < MCOLS; col++)
                {
                    cnt += grid[row, col];
                }
            }
            return(cnt);
        }

        public void moveknot(Knot k1, Knot k2)
        {
            // This is when the head is in a different row than the tail, but same column
            // Move closer by a row
            if ((Math.Abs(k1.x - k2.x) > 1) && (k1.y == k2.y))
            {
                // Move up or down one, depending on whether the head is above or below the tail
                k2.x += (k1.x > k2.x) ? 1 : -1;
            }   
            // This is when the head is in a different column than than the tail, but same row
            // Move closed by a column
            else if ((Math.Abs(k1.y - k2.y) > 1) && (k1.x == k2.x))
            {
                // Move left or right...
                k2.y += (k1.y > k2.y) ? 1 : -1;
            }         
            // This is a different row and column - in which case we move diagonally
            // else if ((iheady != itaily) && (iheadx != itailx)) 
            else if (((Math.Abs(k1.y - k2.y) > 1)) || (Math.Abs(k1.x - k2.x) > 1))
            {
                // In this case, we move both directions...
                k2.y += (k1.y > k2.y) ? 1 : -1;
                k2.x += (k1.x > k2.x) ? 1 : -1;
            }
        }

        public void loadmoves(string file)
        {
            grid[knots[NUMKNOTS - 1].x, knots[NUMKNOTS - 1].y] = 1;

            string[] lines = System.IO.File.ReadAllLines(file);

            foreach (string line in lines)
            {
                string[] flds = line.Split(" ");
                int mv = Int32.Parse(flds[1]);

                // This moves the first knot
                for (int i = 0; i < mv; i++)
                {
                    switch (flds[0])
                    {
                        case "R":
                            knots[0].y += 1;
                            break;
                        case "U":
                            knots[0].x += 1;
                            break;
                        case "L":
                            knots[0].y -= 1;
                            break;
                        case "D":
                            knots[0].x -= 1;
                            break;
                    }
                    // Then cycle through the remaining knots and move accordingly
                    for (int k = 1; k < NUMKNOTS; k++)
                    {
                        moveknot(knots[k-1], knots[k]);
                    }
                    // And track the position of the last knot
                    grid[knots[NUMKNOTS - 1].x, knots[NUMKNOTS - 1].y] = 1;
                }
            }
        }
    }
}
