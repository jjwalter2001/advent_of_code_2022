using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace day09
{

    class Program
    {

        static void Main(string[] args)
        {
            Bridge_part2 t = new Bridge_part2();

            t.loadmoves(@"input.txt");
            Console.WriteLine($"Spots the tail hit:  {t.spotsvisited()}");
        }
    }
}
