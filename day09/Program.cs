using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace day08
{

    public class Bridge
    {
        // Setup a 2 dimensional array the size of the forest.
        const int MROWS = 6;
        const int MCOLS = 6;

        int[,] grid = new int[MROWS, MCOLS];
        int iheadx = 0;
        int itailx = 0;
        int iheady = 0;
        int itaily = 0;

        public void movetail()
        {
            

        }

        public void loadmoves(string file)
        {
            grid[iheadx, iheady] = 1;

            string[] lines = System.IO.File.ReadAllLines(file);

            foreach (string line in lines)
            {
                string[] flds = line.Split(" ");
                int mv = Int32.Parse(flds[1]);

                switch (flds[0])
                {
                    case "R":
                        iheadx += mv;                        
                        break;
                    case "U":
                        iheady += mv;
                        break;
                    case "L":
                        iheadx -= mv;
                        break;
                    case "D":
                        iheady -= mv;
                        break;
                }
                grid[iheadx, iheady] = 1;
            }
        }
    }

    class Program
    {

        static void Main(string[] args)
        {
            Bridge t = new Bridge();

            t.loadmoves(@"sample.txt");
            Console.WriteLine("test");
        }
    }
}
