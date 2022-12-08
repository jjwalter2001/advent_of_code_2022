using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace day08
{

    public class Trees
    {
        // Setup a 2 dimensional array the size of the forest.
        const int MROWS = 99;
        const int MCOLS = 99;

        int[,] trees = new int[MROWS, MCOLS];

        public void loadtrees(string file)
        {
            string[] lines = System.IO.File.ReadAllLines(file);

            // Display the file contents by using a foreach loop.
            int linecnt = 0;
            foreach (string line in lines)
            {
                for (int col = 0; col < line.Length; col++)
                {
                    trees[linecnt, col] = Int32.Parse(line[col].ToString());
                }
                linecnt++;
            }
        }

        // Each of these functions calculates the viewing distance
        // in each direction from the given tree.  The viewing distance
        // is essentially the number of trees until we find one of the same
        // or larger height.
        private int viewlengthtop(int row, int col)
        {
            for (int i = row - 1; i >= 0; i--)
                if (trees[i, col] >= trees[row, col])
                    return row - i;
            return row;
        }

        private int viewlengthbottom(int row, int col)
        {
            for (int i = row + 1; i < MROWS; i++)
                if (trees[i, col] >= trees[row, col])
                    return i - row;
            return MROWS - row - 1;
        }

        private int viewlengthleft(int row, int col)
        {
            // For this, go across cols from 0 to the current position
            for (int i = col - 1; i >= 0; i--)
                if (trees[row, i] >= trees[row, col])
                    return col - i;
            return col;
        }

        private int viewlengthright(int row, int col)
        {
            // For this, go across cols from the current position to the edge
            for (int i = col + 1; i < MCOLS; i++)
                if (trees[row, i] >= trees[row, col])
                    return i - col;
            return MCOLS - col - 1;
        }

        // These functions determine if a tree has a view to the edge of the forest - 
        // i.e., whether every tree in a given direction is shorted than the
        // selected tree.
        private bool isvisiblefromtop(int row, int col)
        {
            // For this, go down rows from 0 to the current position
            for (int i = 0; i < row; i++)
                if (trees[i, col] >= trees[row, col])
                    return false;
            return true;
        }

        private bool isvisiblefrombottom(int row, int col)
        {
            // For this, go down rows from the current position to the edge
            for (int i = row + 1; i < MROWS; i++)
                if (trees[i, col] >= trees[row, col])
                    return false;
            return true;
        }

        private bool isvisiblefromleft(int row, int col)
        {
            // For this, go across cols from 0 to the current position
            for (int i = 0; i < col; i++)
                if (trees[row, i] >= trees[row, col])
                    return false;
            return true;
        }

        private bool isvisiblefromright(int row, int col)
        {
            // For this, go across cols from the current position to the edge
            for (int i = col + 1; i < MCOLS; i++)
                if (trees[row, i] >= trees[row, col])
                    return false;
            return true;
        }

        public bool istreevisible(int row, int col)
        {
            // For the given tree, look each way up, down, and across
            // the array and see if any other tree is the same or larger

            // If on the edge, then it is visible
            if ((row == 0) || (row == MROWS) || (col == 0) || (col == MCOLS))
                return true;

            if (isvisiblefromleft(row, col)
                || isvisiblefrombottom(row, col)
                || isvisiblefromright(row, col)
                || isvisiblefromtop(row, col))
                return true;

            return false;
        }

        public int scenicscore(int row, int col)
        {
            // If on the edge, then the score is zero
            if ((row == 0) || (row == MROWS - 1) || (col == 0) || (col == MCOLS - 1))
                return 0;

            // Otherwise, get the viewing distances in each direction
            // and multiple them out.
            int bot = viewlengthbottom(row, col);
            int top = viewlengthtop(row, col);
            int left = viewlengthleft(row, col);
            int right = viewlengthright(row, col);

            return (bot * top * left * right);
        }

        public int bestscenicscore()
        {
            int bestscore = 0;
            for (int row = 0; row < MROWS; row++)
            {
                for (int col = 0; col < MCOLS; col++)
                {
                    int score = scenicscore(row, col);
                    if (score > bestscore)
                        bestscore = score;
                }
            }
            return (bestscore);
        }

        public int numvisible()
        {
            int num = 0;
            for (int row = 0; row < MROWS; row++)
            {
                for (int col = 0; col < MCOLS; col++)
                {
                    num += istreevisible(row, col) ? 1 : 0;
                }
            }
            return (num);
        }
    }

    class Program
    {

        static void Main(string[] args)
        {
            Trees t = new Trees();

            t.loadtrees(@"input.txt");

            Console.WriteLine($"Num visible trees: {t.numvisible()}");
            Console.WriteLine($"Best scenic score: {t.bestscenicscore()}");
        }
    }
}
