using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace day09
{
    public class Bridge_part1
    {
        // Setup a 2 dimensional array the size of the forest.
        const int MROWS = 999;
        const int MCOLS = 999;

        int[,] grid = new int[MROWS, MCOLS];
        int iheadx = 499;
        int itailx = 499;
        int iheady = 499;
        int itaily = 499;

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

        public void movetail()
        {
            // This is when the head is in a different row than the tail, but same column
            // Move closer by a row
            if ((Math.Abs(iheadx - itailx) > 1) && (iheady == itaily))
            {
                // Move up or down one, depending on whether the head is above or below the tail
                itailx += (iheadx > itailx) ? 1 : -1;
            }   
            // This is when the head is in a different column than than the tail, but same row
            // Move closed by a column
            else if ((Math.Abs(iheady - itaily) > 1) && (iheadx == itailx))
            {
                // Move left or right...
                itaily += (iheady > itaily) ? 1 : -1;
            }         
            // This is a different row and column - in which case we move diagonally
            // else if ((iheady != itaily) && (iheadx != itailx)) 
            else if (((Math.Abs(iheady - itaily) > 1)) || (Math.Abs(iheadx - itailx) > 1))
            {
                // In this case, we move both directions...
                itaily += (iheady > itaily) ? 1 : -1;
                itailx += (iheadx > itailx) ? 1 : -1;
            }
        }

        public void loadmoves(string file)
        {
            grid[itailx, itaily] = 1;

            string[] lines = System.IO.File.ReadAllLines(file);

            foreach (string line in lines)
            {
                string[] flds = line.Split(" ");
                int mv = Int32.Parse(flds[1]);

                for (int i = 0; i < mv; i++)
                {
                    switch (flds[0])
                    {
                        case "R":
                            iheady += 1;                       
                            break;
                        case "U":
                            iheadx -= 1;
                            break;
                        case "L":
                            iheady -= 1;
                            break;
                        case "D":
                            iheadx += 1;
                            break;
                    }
                    movetail();
                    grid[itailx, itaily] = 1;
                }
            }
        }
    }
}
